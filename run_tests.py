try:
    import tests.test_inventory_manager
    import tests.test_product_database
    import tests.test_recipe_database
    import tests.test_robot

    print("✅ All tests have been run successfully!")
except AssertionError as e:
    print("❌ A test failed:", e)
except Exception as e:
    print("⚠️ An error occurred while running tests:", e)