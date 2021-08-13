from django.db import models

# Create your models here.
	

class vertical_farm_1(models.Model):
    idVf1 = models.AutoField(db_column='idVf1', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)

class vertical_farm_2(models.Model):
    idVf2 = models.AutoField(db_column='idVf2', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_3(models.Model):
    idVf3 = models.AutoField(db_column='idVf3', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_4(models.Model):
    idVf4 = models.AutoField(db_column='idVf4', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_5(models.Model):
    idVf5 = models.AutoField(db_column='idVf5', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_6(models.Model):
    idVf6 = models.AutoField(db_column='idVf6', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_7(models.Model):
    idVf7 = models.AutoField(db_column='idVf7', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_8(models.Model):
    idVf8 = models.AutoField(db_column='idVf8', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_9(models.Model):
    idVf9 = models.AutoField(db_column='idVf9', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class vertical_farm_10(models.Model):
    idVf10 = models.AutoField(db_column='idVf10', primary_key=True)  # Field name uppercase.
    Available_capacity = models.IntegerField(blank=True, null=True)
	
class produce_orders(models.Model):
	idOrder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name uppercase.
	Produce_type = models.CharField(max_length=45)
	Qty = models.IntegerField(blank=True, null=True)
	Vf_Order = models.CharField(max_length=45)
	Deliver_Date = models.DateField()
	Deliver_To = models.CharField(max_length=45)
	Customer = models.CharField(max_length=45)
	Customer_Email = models.CharField(max_length=100)
	Key_Value_Pair = models.CharField(max_length=45)

class rest1(models.Model):
	Nomenclature = models.CharField(max_length=25)
	Qty = models.IntegerField(blank=True, null=True)
	Unit = models.CharField(max_length=5)
	Deliver = models.DateField()
	PLU = models.IntegerField(blank=True, null=True)
	Price = models.CharField(max_length=15)
	Total = models.CharField(max_length=15)
	
class Meta:
	managed = True
	db_table = 'vertical_farm_1'

class Meta:
	managed = True
	db_table = 'vertical_farm_2'

class Meta:
	managed = True
	db_table = 'vertical_farm_3'

class Meta:
	managed = True
	db_table = 'vertical_farm_4'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_5'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_6'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_7'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_8'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_9'
	
class Meta:
	managed = True
	db_table = 'vertical_farm_10'
	
class Meta:
	#managed = True
	db_table = 'produce_orders'
	
def __str__(self):
	return self.name