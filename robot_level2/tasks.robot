*** Settings ***
Documentation       Template robot main suite.

Library    tasks.py

*** Tasks ***
Minimal task
    # Minimal Task
    order robots from RobotSpareBin
    
