# import math
#
# from behave import *
#
#
# @Given('I have a positive integer {i:d}')
# def step_impl(context, i):
#     context.i = i
#
#
# @When('calculate factorial')
# def step_impl(context):
#     context.f = math.factorial(context.i)
#
#
# @Then('I get a factorial of the integer {f:d}')
# def step_impl(context, f):
#     assert f == context.f
