from exercises.models import Book, Author, Classification


c1 = Classification.objects.create(code='001', name='name1', description='description1')
c2 = Classification.objects.create(code='002', name='name2', description='description2')
c3 = Classification.objects.create(code='003', name='name3', description='description3')


a1 = Author.objects.create(full_name='Full N. Name')
a2 = Author.objects.create(full_name='Name N. Name')


Book.objects.create(title='Book 1', author=a1, classification=c1)
Book.objects.create(title='Book 2', author=a2, classification=c1)
Book.objects.create(title='Book 3', author=a1, classification=c2)

Book.objects.create(title='Book 4', author=a2, classification=c3)
