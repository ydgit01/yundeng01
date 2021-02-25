def pytest_configure(config):
    marker_list = ["allure_label.feature","allure_label.story","allure_title","allure_step",
                   "allure_description","allure_link_issue","allure_test_test"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )