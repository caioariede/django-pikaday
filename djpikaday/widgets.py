import os.path
import glob

from django.forms import Media, DateInput
from django.core.urlresolvers import reverse, NoReverseMatch
from django.conf import settings

from django.utils.translation import get_language
from django.utils.formats import get_format


DJPIKADAY = getattr(settings, 'DJPIKADAY', {})
DJPIKADAY_LOAD_JSI18N = DJPIKADAY.get('LOAD_JSI18N', True)
DJPIKADAY_DATE_INPUT_FORMAT = DJPIKADAY.get('DATE_INPUT_FORMAT')


MOMENT_LANG_FILES = map(
    lambda s: os.path.basename(s)[:-3],
    glob.glob(
        os.path.sep.join([
            os.path.dirname(__file__),
            'static', 'moment', 'lang', '*.js'
        ])))


class PikadayInput(DateInput):
    def _media(self):
        css = {
            'all': (
                'pikaday/css/pikaday.css',
            ),
        }

        js = []

        # i18n
        load_i18n = True

        if DJPIKADAY_LOAD_JSI18N:
            try:
                js.append(reverse('django.views.i18n.javascript_catalog'))
            except NoReverseMatch:
                load_i18n = False

        # moment
        js.append('moment/moment.js')

        # moment lang file
        if load_i18n:
            lang = get_language()
            if lang in self.get_moment_lang_files():
                js.append('moment/lang/' + lang + '.js')

        # pikaday
        js.append('pikaday/pikaday.js')
        js.append('js/djpikaday.js')

        return Media(css=css, js=js)

    media = property(_media)

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        attrs['data-pikaday'] = 'true'
        attrs['data-moment-format'] = self.get_moment_format()

        return super(PikadayInput, self).render(name, value, attrs)

    def get_format(self):
        return DJPIKADAY_DATE_INPUT_FORMAT or self.format

    def get_moment_format(self):
        """
        Converting Python format:
        http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
        
        To Moment format:
        http://momentjs.com/docs/#/displaying/format/

        Not all directives are supported (only those date-related)
        """
        fmt = self.get_format()

        fmt = fmt.replace(r'%a', 'ddd')
        fmt = fmt.replace(r'%A', 'dddd')
        fmt = fmt.replace(r'%w', 'd')
        fmt = fmt.replace(r'%d', 'DD')
        fmt = fmt.replace(r'%b', 'MMM')
        fmt = fmt.replace(r'%B', 'MMMM')
        fmt = fmt.replace(r'%m', 'MM')
        fmt = fmt.replace(r'%y', 'YY')
        fmt = fmt.replace(r'%Y', 'YYYY')
        fmt = fmt.replace(r'%j', 'DDDD')
        fmt = fmt.replace(r'%U', 'ww')
        fmt = fmt.replace(r'%x', 'L')

        return fmt

    def get_moment_lang_files(self):
        return MOMENT_LANG_FILES
