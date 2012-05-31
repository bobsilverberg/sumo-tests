#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import pytest
import requests
import urllib


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestRedirects:

    _user_agent_firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:12.0) Gecko/20100101 Firefox/12.0'

    def _check_redirect(self, testsetup, start_url, user_agent=_user_agent_firefox, locale='en-US'):
        start_url = testsetup.base_url + start_url

        headers = {'user-agent': user_agent,
                   'accept-language': locale}
        return requests.get(start_url, headers=headers)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/1/firefox/4.0/WINNT/en-US/firefox-help/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/WINNT/en-US/firefox-f1/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/WINNT/en-US/firefox-osxkey/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Darwin/en-US/firefox-help/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Darwin/en-US/firefox-f1/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Darwin/en-US/firefox-osxkey/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Linux/en-US/firefox-help/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Linux/en-US/firefox-f1/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/Linux/en-US/firefox-osxkey/', '/en-US/home?as=u'),
        ('/1/firefox/4.0/WINNT/en-US/prefs-main/', '/en-US/kb/startup-home-page-download-settings?redirectlocale=en-US&as=u&redirectslug=Options+window+-+General+panel'),
        ('/1/firefox/4.0/Darwin/en-US/prefs-main/', '/en-US/kb/startup-home-page-download-settings?redirectlocale=en-US&as=u&redirectslug=Options+window+-+General+panel'),
        ('/1/firefox/4.0/Linux/en-US/prefs-main/', '/en-US/kb/startup-home-page-download-settings?redirectlocale=en-US&as=u&redirectslug=Options+window+-+General+panel'),
        ('/1/firefox/4.0/WINNT/en-US/prefs-clear-private-data/', '/en-US/kb/remove-recent-browsing-search-and-download-history?redirectlocale=en-US&as=u&redirectslug=Clear+Recent+History'),
        ('/1/firefox/4.0/Darwin/en-US/prefs-clear-private-data/', '/en-US/kb/remove-recent-browsing-search-and-download-history?redirectlocale=en-US&as=u&redirectslug=Clear+Recent+History'),
        ('/1/firefox/4.0/Linux/en-US/prefs-clear-private-data/', '/en-US/kb/remove-recent-browsing-search-and-download-history?redirectlocale=en-US&as=u&redirectslug=Clear+Recent+History'),
        ('/1/firefox/4.0/WINNT/en-US/prefs-fonts-and-colors/', '/en-US/kb/settings-fonts-languages-pop-ups-javascript?redirectlocale=en-US&as=u&redirectslug=Options+window+-+Content+panel#fonts_and_colors')])
    def test_browser_redirect_to_sumo(self, mozwebqa, input, expected):
        expected_url = mozwebqa.base_url + expected
        r = self._check_redirect(mozwebqa, input)

        Assert.equal(urllib.unquote(r.url), expected_url)
        Assert.equal(r.status_code, requests.codes.ok)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/1/mobile/4.0/android/en-US/firefox-help', '/en-US/mobile?as=u'),
        ('/1/mobile/4.0/iphone/en-US/firefox-help', '/en-US/mobile?as=u'),
        ('/1/mobile/4.0/nokia/en-US/firefox-help', '/en-US/mobile?as=u')])
    def test_old_mobile_redirects(self, mozwebqa, input, expected):
        expected_url = mozwebqa.base_url + expected
        r = self._check_redirect(mozwebqa, input)

        Assert.equal(urllib.unquote(r.url), expected_url)
        Assert.equal(r.status_code, requests.codes.ok)

    @pytest.mark.parametrize(('input', 'expected'), [
        ('/1/firefox-home/4.0/iPhone/en-US', '/en-US/kb/what-is-firefox-home-for-ios-iphone-and-ipad?redirectlocale=en-US&as=u&redirectslug=What+is+Firefox+Home'),
        ('/1/firefox-home/4.0/iPhone/en-US/log-in', '/en-US/kb/Cannot log in to Firefox Home App?as=u')])
    def test_iphone_redirects(self, mozwebqa, input, expected):
        expected_url = mozwebqa.base_url + expected
        r = self._check_redirect(mozwebqa, input)

        Assert.equal(urllib.unquote(r.url), expected_url)
        Assert.equal(r.status_code, requests.codes.ok)