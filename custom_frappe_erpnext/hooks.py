app_name = "custom_frappe_erpnext"
app_title = "Custom App"
app_publisher = "Alex"
app_description = "custom frappe erpnext app"
app_email = "alex123@gmail.com"
app_license = "mit"


fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Invoice-custom_company_name",
                ],
            ]
        ],
    },
    {
        "dt": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Order-tax_id-label",
                    "Address-address_type-label",
                ],
            ]
        ],
    },
]
