
### 📌 What is a Vendor Purchase Order?

* A **Vendor Purchase Order (PO)** is a formal document issued by a **company (buyer)** to its **vendor/supplier** to procure goods or services.
* It specifies **item details, quantities, prices, delivery terms, and PO number**.
* In ERP systems, the vendor PO is the **starting point for procurement and Accounts Payable (AP)** processes.

---

### 🔄 How it works in the ERP world

1. **PO Creation (Procure-to-Pay Initiation)**

   * Internal demand (via requisition, MRP run, or planner) triggers the creation of a **Vendor PO**.
   * ERP captures: **vendor ID, items, qty, unit price, expected delivery date, ship-to address**.
   * Approval workflows may route the PO to managers before release.

2. **PO Dispatch**

   * Once approved, the PO is formally sent to the vendor (via EDI, email, portal, etc.).
   * Vendor acknowledges receipt and confirms pricing and delivery schedules.

3. **Goods/Services Delivery**

   * Vendor ships goods or provides services as per the PO.
   * ERP logs **Goods Receipt (GR)** or **Service Entry Sheet (SES)** against the PO.
   * Inventory levels are updated automatically upon GR.

4. **3-Way Match**

   * ERP performs a **3-way match** between:

     * **PO** (what was ordered)
     * **Goods Receipt** (what was received)
     * **Vendor Invoice** (what was billed)
   * Any mismatches (qty/price differences) are flagged for resolution.

5. **Invoice Processing**

   * Vendor sends invoice referencing the PO.
   * ERP creates **AP Invoice** linked to the PO.
   * After successful 3-way match, invoice is approved for payment.

6. **Payment & Settlement**

   * ERP processes payment per agreed terms (e.g., Net 30, Net 60).
   * Payment can be via check, ACH, wire, etc.
   * ERP posts to **General Ledger (GL)**:

     * Debit **AP / Expense / Inventory**
     * Credit **Cash / Bank**

7. **Auditing & Reporting**

   * Vendor PO provides audit trail for compliance (e.g., SOX).
   * ERP reporting uses POs for:

     * Supplier performance (on-time delivery, quality)
     * Spend analysis (by category, vendor, region)
     * Cash flow forecasting (AP aging, outstanding liabilities)

---


Would you like me to also make a **side-by-side comparison table** of **Customer PO vs Vendor PO in ERP** (so you can see the O2C vs P2P differences at a glance)?
