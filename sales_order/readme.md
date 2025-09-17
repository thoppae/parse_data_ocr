

### 📌 What is a Customer Purchase Order and how its convered to Sales Order?

* A **Customer Purchase Order (PO)** is a **formal document issued by a buyer (customer)** to a seller (supplier/vendor) indicating the products or services they want to purchase.
* It includes **details like items, quantities, pricing, delivery address, payment terms, and PO number**.
* In the ERP system, the PO acts as the **official trigger** for order fulfillment and financial processes.

---

### 🔄 How it works in the ERP world

1. **PO Creation**

   * Customer issues a PO to the supplier.
   * ERP captures key details: **PO number, customer name, items, quantity, price, ship-to, and billing information**.

2. **Order Entry (Sales Order Creation)**

   * In many ERP systems, the **customer PO → Sales Order (SO)**.
   * The ERP validates the PO against:

     * **Master data** (customer records, SKU catalog, pricing).
     * **Credit limits or approval workflows**.
   * Once validated, the PO data is transformed into an **SO payload** ready for processing.

3. **Order Processing**

   * ERP schedules fulfillment (inventory allocation, warehouse picking).
   * Shipping details and expected delivery dates are managed in the system.

4. **Fulfillment**

   * Items are shipped or services delivered.
   * ERP updates the SO status → **Shipped / Partially Shipped**.
   * Generates supporting docs: **Advance Shipment Notice (ASN), packing slip, shipping labels**.

5. **Invoicing**

   * Based on the shipment, the ERP generates a **customer invoice**.
   * Links back to the original PO → ensuring traceability and reconciliation.

6. **Payment & Settlement**

   * Customer pays the invoice (per terms like Net 30, Net 60, etc.).
   * ERP updates **Accounts Receivable (AR)** and posts entries to the **General Ledger (GL)**:

     * Debit **Cash/AR**
     * Credit **Revenue**

7. **Auditing & Reporting**

   * PO acts as the **anchor record** for audits.
   * ERP uses PO → SO → Invoice → Payment linkage for:

     * Compliance
     * Operational reporting (e.g., order backlog, fulfillment rates)
     * Financial reporting (e.g., revenue recognition, AR aging).

---


Would you like me to also create a **visual flow diagram (boxes & arrows)** to show PO → SO → Shipment → Invoice → Payment in a way you can drop directly into your documentation?
