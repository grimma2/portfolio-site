from django.db import models
from django.urls import reverse


class Info(models.Model):
    ''' 1 блок инфы про проект с картинкой заоловком и описанием '''
    info_title = models.CharField('Заголовок инфы', max_length = 100)
    info_text = models.TextField('Текст инфы')
    info_image = models.FileField('картинка', upload_to = 'infoimg/', blank = True)

    def __str__(self):
        return self.info_title

    class Meta:
        verbose_name = 'Инфа о нас'
        verbose_name_plural = 'Инфа о нас'

    def get_absolute_url(self):
        return reverse('info', kwargs = {'info_id': self.pk})


class Marafon(models.Model):
    ''' Сам марафон с его описанием в ввиде садий и прайсом '''
    marafon_name = models.CharField('Название марафона', max_length = 255)
    marafon_tiers = models.TextField('Описане марафона')
    total_place = models.PositiveIntegerField('счетчик свободных мест', default = 0)
    marafon_desc = models.TextField('описание всего')
    price = models.PositiveIntegerField('Стоимоть марафона', default = 0)
    slug = models.SlugField(verbose_name = 'URL', max_length = 255, unique = True, db_index = True)

    def __str__(self):
        return self.marafon_name

    class Meta:
        verbose_name = 'марафон'
        verbose_name_plural = 'марафоны'

    def get_absolute_url(self):
        return reverse('marafon', kwargs = {'marafon_slug': self.pk})


class Faq(models.Model):
    ''' Ответы на самые часто задаваемые вопросы '''
    text_ask = models.CharField('вопрос', max_length = 255)
    text_answer = models.TextField('текст ответа на вопрос')

    def __str__(self):
        return self.text_ask

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def get_absolute_url(self):
        return reverse('faq', kwargs = {'faq_id': self.pk})


class Sponsor(models.Model):
    ''' спонсор и ссылка '''
    title_sponsor = models.CharField('имя спонсора', max_length=255)
    desc_sponsor = models.TextField('Описание спонсора')
    url_image = models.FileField('УРЛ картинки', upload_to= 'sponsorimg/', blank = True)
    link = models.TextField('линк на спонсора')

    def __str__(self):
        return self.title_sponsor

    class Meta:
        verbose_name = 'спонсор'
        verbose_name_plural = 'спонсоры'

    def get_absolute_url(self):
        return reverse('sponsor', kwargs={'sponsor_id': self.pk})
