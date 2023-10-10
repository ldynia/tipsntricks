# Django

### Security

https://www.linkedin.com/pulse/sql-injection-django-applications-jerin-jose

### Signals

```python
import os
import uuid
from app.models.sample import Sample


class SampleAnalysis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'sample_analysis'
        verbose_name = 'Sample Analysis'
        verbose_name_plural = 'Sample Analysis'


# post delete signal
@receiver(post_delete, sender=SampleAnalysis)
def post_delete(sender, **kwargs):
    """ Remove results of sample analysis when the sample is deleted. """
    results_path = kwargs['instance'].results_path
    if results_path:
        command = 'rm -rf ' + results_path
        os.system(command)

```


### Cellery

```python
# get the result of a task if I have the ID that points there?
from app.tasks.analysis import run_pipeline
task = run_pipeline.AsyncResult(task.id)
```


### Caching
```python
CACHE_KEY = 'user_' + str(request.user.id) + '_samples'
files = cache.get(CACHE_KEY)
if not files:
    files = FileUploadRepository().find_all_by(user=request.user, status='complete')
    cache.set(CACHE_KEY, files, TIME_IN_SECONDS['MINUTES'][1])
```

### Deployment uwsgi
```
uwsgi --uid flag --enable-threads --socket app.sock --wsgi-file config/wsgi.py
uwsgi --ini config/services/compare_uwsgi.ini
```

### Upload
```python
/usr/local/lib/python2.7/site-packages/django
/var/lib/wwwrun/chunked_uploads

sftp://vagrant@127.0.0.1:2222/var/lib/wwwrun/chunked_uploads
sftp://vagrant@127.0.0.1:2222/usr/local/lib/python2.7/site-packages/django
```

### Data Dump

```python
python manage.py dumpdata --all > db/test.json
python manage.py loaddata database/dbdump.json
```

### Model interactions

```python
# save values to model
model = UserGroupInviter(group_id=id, user_id=request.user.id, email=request.data['email'])
invitation_is_saved = UserGroupInviterRrepository.save(model)

# save dict to model
model = MyModel(**data_dict)
model = MyModel(extra='hello', **data_dict)
model.save()

Calling .save() will either create a new instance, or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class:

# .save() will create a new instance.
serializer = CommentSerializer(data=data)

# .save() will update the existing `comment` instance.
serializer = CommentSerializer(comment, data=data)
```

### Model callbacks

Before save
```python
class FileUploadMetadata(models.Model):

  latitude = models.FloatField()
  longitude = models.FloatField()

  def save(self, *args, **kwargs):
      # Normalize values before save
      if self.latitude == '' or self.latitude is None:
          self.latitude = 0

      if self.longitude == '' or self.longitude is None:
          self.longitude = 0

      super(FileUploadMetadata, self).save(*args, **kwargs)

```

### Testing

```python
$ python manage.py test tests.core.api.test_user_view
```


### URL
```python
# build url to resource
request.build_absolute_uri(META_DATA_OUTPUT_RELATIVE_PATH)
```

### ORM

```python
# Bulk update dataset
mol_ids = dataset.molecules.all().values_list('id', flat=True)

first_ds_mol_ids = list(mol_ids[:SPLIT_INDEX])
second_ds_mol_ids = list(mol_ids[SPLIT_INDEX:])

Molecule.objects.filter(id__in=first_ds_mol_ids).update(dataset=first_ds.id)
Molecule.objects.filter(id__in=second_ds_mol_ids).update(dataset=second_ds.id)
```

### Others

New Django way for fetching User model.

```python
from django.contrib.auth import get_user_model
some_user = get_user_model().objects.get(email='some@email.com')
```
