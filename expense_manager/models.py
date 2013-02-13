# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


FREQUENCIES = {'1': 'week', '2': 'month'}


class AndroidMetadata(models.Model):
    locale = models.TextField(primary_key=True)

    class Meta:
        db_table = u'android_metadata'

    def __unicode__(self):
        return "Locale: %s" %(self.locale)


class ExpenseBudget(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    account = models.TextField(blank=True)
    no_of_payment = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)
    frequency = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    alert = models.TextField(blank=True)
    description = models.TextField(blank=True)
    property = models.TextField(blank=True)
    modified = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'expense_budget'

    def __unicode__(self):
        return "Budget: %s for %s (%s) per %s" %("${:0,.0f}".format(float(self.amount)), self.category, self.subcategory, FREQUENCIES[self.frequency])


class ExpenseCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)

    class Meta:
        db_table = u'expense_category'

    def __unicode__(self):
        return "Category: %s (%s)" %(self.category, self.subcategory)


class ExpenseNote(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    note_title = models.TextField(blank=True)
    note_content = models.TextField(blank=True)
    note_order = models.TextField(blank=True)
    note_transaction_id = models.TextField(blank=True)
    note_tag = models.TextField(blank=True)
    note_reminder = models.TextField(blank=True)
    status = models.TextField(blank=True)
    property = models.TextField(blank=True)
    modified = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'expense_note'

    def __unicode__(self):
        return "Note: %s (%s)" %(self.note_title, self.note_content)


class ExpensePayeePayer(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    payee_payer = models.TextField(blank=True)
    account = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)
    payment_method = models.TextField(blank=True)
    reference_number = models.TextField(blank=True)
    description = models.TextField(blank=True)
    status = models.TextField(blank=True)
    address = models.TextField(blank=True)
    property = models.TextField(blank=True)
    modified = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'expense_payee_payer'

    def __unicode__(self):
        return "Note: %s (%s)" %(self.payee_payer, self.account)


class ExpensePreference(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    name = models.TextField(blank=True)
    value = models.TextField(blank=True)
    modified = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'expense_preference'

    def __unicode__(self):
        return "Preference: %s (%s)" %(self.name, self.value)


class ExpenseRepeating(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    account = models.TextField(blank=True)
    description = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    no_of_payment = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)
    payment_method = models.TextField(blank=True)
    frequency = models.TextField(blank=True)
    remind_time = models.TextField(blank=True)
    paid_cycle = models.TextField(blank=True)
    property = models.TextField(blank=True)
    next_payment_date = models.IntegerField(null=True, blank=True)
    first_expensed = models.IntegerField(null=True, blank=True)
    modified = models.IntegerField(null=True, blank=True)
    status = models.TextField(blank=True)
    property2 = models.TextField(blank=True)
    property3 = models.TextField(blank=True)

    class Meta:
        db_table = u'expense_repeating'


class ExpenseReport(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    account = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)
    payment_method = models.TextField(blank=True)
    description = models.TextField(blank=True)
    expensed = models.IntegerField(null=True, blank=True)
    modified = models.IntegerField(null=True, blank=True)
    reference_number = models.TextField(blank=True)
    property = models.TextField(blank=True)
    status = models.TextField(blank=True)
    property2 = models.TextField(blank=True)

    class Meta:
        db_table = u'expense_report'

    def __unicode__(self):
        return "Expense: %s on %s (%s)" %("${:0,.0f}".format(float(self.amount)), self.category, self.subcategory)

