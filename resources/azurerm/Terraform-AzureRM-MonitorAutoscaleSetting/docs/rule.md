# Terraform::AzureRM::MonitorAutoscaleSetting Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ <a href="rule-metrictrigger.md">MetricTrigger</a>, ... ]</i>,
    "<a href="#scaleaction" title="ScaleAction">ScaleAction</a>" : <i>[ <a href="rule-scaleaction.md">ScaleAction</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - <a href="rule-metrictrigger.md">MetricTrigger</a></i>
<a href="#scaleaction" title="ScaleAction">ScaleAction</a>: <i>
      - <a href="rule-scaleaction.md">ScaleAction</a></i>
</pre>

## Properties

#### MetricTrigger

_Required_: No

_Type_: List of <a href="rule-metrictrigger.md">MetricTrigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleAction

_Required_: No

_Type_: List of <a href="rule-scaleaction.md">ScaleAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
