
### 📌 What is a Customer Invoice?

* A **Customer Invoice** is a formal billing document issued by the seller to the customer after goods or services have been shipped/delivered.
* It is directly linked to the **Customer Purchase Order** and the **Sales Order** in the ERP system.
* Acts as the **trigger for Accounts Receivable (AR)** and revenue recognition.

---

### 🔄 How it works in ERP

1. **Invoice Creation**

   * Triggered automatically after **Item Fulfillment / Shipment** on a Sales Order.
   * Contains: **SO reference, items, quantities shipped, unit prices, taxes, shipping charges, payment terms**.
   * Can be created as:

     * **Full Invoice** (all items shipped)
     * **Partial Invoice** (partial fulfillment)

2. **Impact on Sales Order (SO)**

   * When invoice is generated, the linked SO lines are updated:

     * **Invoiced Qty** field increases.
     * If all items are invoiced and shipped → SO status changes to **Closed**.
     * If partially invoiced → SO remains **Open / Partially Fulfilled**.

3. **Impact on Item Fulfillment**

   * Each **Item Fulfillment (IF)** is linked to the corresponding invoice.
   * Once invoiced, the IF record is marked **Billed**.
   * Ensures traceability: PO → SO → IF → Invoice.

4. **Impact on Accounts Receivable (AR)**

   * Invoice creation posts entries to **AR subledger**:

     * **Debit Accounts Receivable** (customer owes)
     * **Credit Revenue** (income recognized)
   * Tax, shipping, or discounts are also posted accordingly.

5. **Impact on General Ledger (GL)**

   * Journal entries from AR flow into GL:

     * **Debit AR / Customer Account**
     * **Credit Revenue**
     * (Optionally, **Credit Tax Payable** if applicable)

6. **Payment Tracking**

   * When customer payment is received:

     * **Debit Cash / Bank**
     * **Credit AR**
   * ERP updates invoice status: **Open → Paid**.
   * Once all invoices tied to an SO are paid, the order lifecycle is fully complete.

7. **Reporting & Audit**

   * Customer invoices feed into:

     * **AR Aging Reports** (open receivables, overdue amounts)
     * **Revenue Reports** (sales by product, region, customer)
     * **Audit Trail** linking SO → Fulfillment → Invoice → Payment

---

✅ **In short:**
A **customer invoice closes the revenue side of the Sales Order cycle**:

* Operationally → ties shipments to billing and closes SOs when fully invoiced.
* Financially → creates AR, recognizes revenue, and updates the GL.

---

