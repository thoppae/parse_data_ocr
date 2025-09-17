

# PO/Invoice → SO Pipeline (GCP → Google Sheets / ERP)

This project ingests **PDF purchase orders or invoices** from Google Cloud Storage (GCS), parses them to a clean JSON, grounds the data with Google Sheets master data, validates business rules, and then posts orders to either a **mock ERP tab in Sheets** or a **real ERP webhook**.

> Example documents like the “Top Repair LLC” receipt are normalized from noisy OCR output into a compact, processable JSON.&#x20;

---

## Step-by-Step

### 1) Prepare Google Cloud & Sheets

* Create/identify a **GCP project** and a **GCS bucket** for incoming PDFs.
* Create a **Google Sheet** with:

  * **Customers** tab: `customer_name | customer_id | customer_ship_to_address`
  * **SKU’s** tab: `sku_ref | description | unit_price | category | inventory_location`
* Create a **Service Account**, share the Sheet with it (Editor), and grant it read access to your GCS bucket.

### 2) Drop PDFs into GCS

* Place source **PDFs (POs or invoices)** into your GCS bucket (e.g., `gs://…/incoming/`).
* (Optional) Add a folder convention (e.g., `po/`, `invoice/`) for downstream routing.

### 3) OCR to JSON (optional but recommended)

* Run **Document AI** (or your OCR tool) to convert PDFs → raw JSON.
* Store the raw OCR JSON alongside the PDF in GCS (e.g., `…/incoming/*.json`).

### 4) Sanitize to a Clean Pre-Model

* Convert noisy OCR output to a compact, consistent JSON (“**PreModel**”):

  * For **POs**: `po_number`, `po_date`, `customer_name`, `currency`, `lines[] {sku_ref, qty, unit_price}`, plus optional `notes`/`problems`.
  * For **invoices/receipts**: normalize vendor, date, totals, and line items into a consistent shape.
* Strip any extra characters or layout artifacts so it’s valid JSON and easy to parse.

### 5) Ground with Master Data (Google Sheets)

* **Match** `customer_name → customer_id` and **enrich** with `ship_to_address` from the **Customers** tab.
* **Match** `sku_ref → sku_id` and **enrich** each line with `description`, `unit_price` (as contract/list), `category`, and `inventory_location` from the **SKU’s** tab.
* Produce a **Sales Order payload (SO)**:

  * Header: `customer_id`, `po_number`, `currency`, `ship_to_address`, `customer_name`
  * Lines: `sku_id`, `sku_ref`, `description`, `qty`, `unit_price`, `contract_price_applied`, `category`, `inventory_location`, `uom`
  * Totals: `total_amount`

### 6) Validate (Schema + Business Rules)

* **Schema**: required fields, types, formats (e.g., currency string, lines present).
* **Business rules** (examples):

  * Currency whitelist (e.g., `USD`, `EUR`).
  * `qty > 0`, `unit_price ≥ 0`.
  * **Price tolerance** check: `abs(unit_price − contract_price_applied) ≤ threshold`.
  * `inventory_location` required per line.
  * Total recomputation must match `total_amount`.
* Decide whether failures **block** posting or get **routed to a review queue**.

### 7) Exceptions & Review (recommended)

* If schema/business validation fails, **append** the record to a **Review\_Queue** tab with the error list.
* Human reviewers correct data (e.g., fix SKU, address, or price) and re-run.

### 8) Post to ERP Target

* **Option A (Mock ERP in Sheets):** Append each SO line to an **`ERP_Orders`** tab with columns:

  * `po_number | customer_id | customer_name | ship_to_address | currency | line_no | sku_id | sku_ref | description | qty | unit_price | contract_price | extended_amount | category | inventory_location | total_amount | status`
* **Option B (Real ERP):** Send the finalized **SO payload** via HTTP POST to your ERP endpoint. Capture ERP confirmation IDs in the Sheet for traceability.

### 9) Logging & Audit (minimum viable)

* Record run timestamp, input source (GCS path), and a hash or ID of the pre-model JSON.
* Log any warnings/errors and who posted the order (service account vs. user).

### 10) Security & Compliance (MVP posture)

* Keep service account credentials in **Secret Manager** or use **Workload Identity**.
* Restrict Sheet sharing to least privilege.
* If handling PII, confirm acceptable storage, retention, and access review practices before production.

### 11) Operations & Scaling (later)

* Replace manual triggers with:

  * **GCS notifications** → Pub/Sub → Cloud Run job to auto-process new PDFs.
  * Daily **health checks** (counts, error rates, spend).
* Add **unit tests** for sanitization, grounding, and validation rules.
* Promote from Colab/notebook to **Cloud Run** (FastAPI) if you need a shared UI or API.

---

## Success Criteria (MVP)

* A PDF placed in GCS is **parsed**, **grounded**, **validated**, and **posted** to `ERP_Orders` (or your ERP webhook) with a complete audit trail.
* Exceptions never disappear: they **land in Review\_Queue** with clear, actionable reasons.

---

If you’d like, I can condense this into a one-page checklist version for the very top of your README, or add a short “Glossary” section (PreModel, Grounding, ERP Mock, etc.).
