# jmad/tests.py
    # functional test
        - test_student_find_solos

# create solos app
# create solos/tests
    # add solos/tests/test_urls.py
        - test_root_url_uses_index_view
    # add solos/tests/test_views.py
        - test_index_view_basic

# create solos/templates/solos/index.html
    # functional test on form submission and catching results
    # add to solos/tests/test_views.py
        - test_index_view_returns_solos

# create solos/tests/test_models.py
    # create SoloModelTestCase class
        - setUp Solo.objects.create
        - add test_solo_basic
# create Solo model


page 107
