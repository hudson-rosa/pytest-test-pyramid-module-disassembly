Feature: Dashboard UI Smoke Test
  As an operator
  I want to open the dashboard
  So that I can see the system status

  @ui @smoke
  Scenario: Dashboard loads successfully
    Given the operator is on the dashboard page
    Then the page title should "Battery Lifecycle Dashboard"
    And the system status indicator shows "The system is operational"

  @ui @module-status
  Scenario: Dashboard shows the module results
    Given the operator is on the dashboard page
    And the system status indicator is "The system is operational"
    When the operator enters module number "20260130"
    And clicks the [Check Status] button
    Then the module status shows "MODULE PROCESSED"