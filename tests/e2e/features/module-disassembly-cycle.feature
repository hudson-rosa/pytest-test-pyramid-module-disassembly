Feature: Module processing
  As an operator
  I want the system to process a module correctly
  So that a valid image is captured and the module exits the system

  @e2e @happy-path
  Scenario: Successful module disassembly cycle
    Given the system is ready
    When a cycle is started
    And an image is captured with a module
    Then the module is processed successfully
