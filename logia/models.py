from django.db import models

class PatientsModel(models.Model):
    class Meta:
        db_table = 'patients'

    uuid = models.CharField(max_length=256)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=str(), blank=True)

    def __str__(self) -> str:
        return f'{self.uuid}, {self.first_name}, {self.last_name}, {self.date_of_birth}'


class PharmaciesModel(models.Model):
    class Meta:
        db_table = 'pharmacies'

    uuid = models.CharField(max_length=256)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.uuid}, {self.name}, {self.city}'


class TransactionsModel(models.Model):
    class Meta:
        db_table = 'transactions'

    uuid = models.CharField(max_length=256)
    patient_uuid = models.ForeignKey(PatientsModel, on_delete=models.DO_NOTHING)
    pharmacy_uuid = models.ForeignKey(PharmaciesModel, on_delete=models.DO_NOTHING)
    amount = models.FloatField(null=True, blank=True)
    timestamp = models.DateField(default=str(), blank=True)


class UsersModel(models.Model):
    class Meta:
        db_table = 'users'

    uuid = models.CharField(max_length=256)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    