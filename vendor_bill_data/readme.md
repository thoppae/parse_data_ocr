
### 📌 What is a Vendor Bill?

* A **Vendor Bill** is the billing document received from a supplier after goods or services have been delivered.
* It references the company’s **Vendor Purchase Order (PO)** and **Goods Receipt / Item Receipt** in the ERP system.
* It is the trigger for **Accounts Payable (AP)** processing and expense or inventory recognition.

---

### 🔄 How it works in ERP

1. **Bill Receipt**

   * Vendor sends their bill referencing the PO number.
   * ERP captures key details: **PO reference, items, quantities, unit prices, taxes, shipping, payment terms**.
   * Bill is logged into AP as **Unapproved / Pending Match**.

2. **Impact on Purchase Order (PO)**

   * The PO record is updated with **Billed Quantity** or **Invoiced Amount**.
   * If all lines are received and billed → PO status changes to **Closed**.
   * If partially billed → PO remains **Open / Partially Billed**.

3. **Impact on Goods Receipt / Item Receipt**

   * ERP performs a **3-way match**:

     * **PO** (what was ordered)
     * **Goods Receipt** (what was received)
     * **Vendor Bill** (what was billed)
   * If matched → Item Receipt is marked as **Billed**.
   * Discrepancies trigger **Exceptions** for review (qty/price mismatch).

4. **Impact on Accounts Payable (AP)**

   * Approved bill posts to AP subledger:

     * **Debit Inventory** (if goods) or **Expense** (if services)
     * **Credit Accounts Payable** (liability owed to vendor)

5. **Impact on General Ledger (GL)**

   * The AP entry flows to GL:

     * **Debit Inventory / Expense**
     * **Credit Accounts Payable**
   * Taxes, freight, or discounts are also posted accordingly.

6. **Payment Processing**

   * When company pays the vendor:

     * **Debit Accounts Payable**
     * **Credit Cash / Bank**
   * ERP updates bill status: **Open → Paid**.
   * Once all bills against a PO are paid, the PO lifecycle is fully complete.

7. **Reporting & Audit**

   * Vendor bills feed into:

     * **AP Aging Reports** (outstanding liabilities, overdue bills)
     * **Spend Reports** (cost by category, vendor, department)
     * **Audit Trail** linking PO → Item Receipt → Vendor Bill → Payment

---

✅ **In short:**
A **vendor bill closes the liability side of the Purchase Order cycle**:

* Operationally → ties receipts to billing and closes POs when fully billed.
* Financially → creates AP liability, recognizes inventory/expenses, and updates the GL.

----
