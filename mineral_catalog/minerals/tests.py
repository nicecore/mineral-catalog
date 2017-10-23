from django.test import TestCase
from .models import Mineral
from django.core.urlresolvers import reverse


class MineralViewTests(TestCase):

    def setUp(self):
        self.adamite = Mineral.objects.create(name='Adamite')
        self.ryanite = Mineral.objects.create(name='Ryanite')


    def test_mineral_list(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.adamite, resp.context['minerals'])
        self.assertIn(self.ryanite, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')


    def test_mineral_detail(self):
        resp = self.client.get(
            reverse('minerals:detail', kwargs={'pk': self.adamite.pk})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.adamite.name, resp.context['mineral'].values())
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')