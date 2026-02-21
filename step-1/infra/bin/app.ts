#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { CalculatorStack } from "../lib/calculator-stack";

const app = new cdk.App();

new CalculatorStack(app, "CalculatorStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: "us-east-1",
  },
});
