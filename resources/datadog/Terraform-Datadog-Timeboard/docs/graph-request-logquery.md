# Terraform::Datadog::Timeboard Graph Request LogQuery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#index" title="Index">Index</a>" : <i>String</i>,
    "<a href="#compute" title="Compute">Compute</a>" : <i>[ <a href="graph-request-logquery-compute.md">Compute</a>, ... ]</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="graph-request-logquery-groupby.md">GroupBy</a>, ... ]</i>,
    "<a href="#search" title="Search">Search</a>" : <i>[ <a href="graph-request-logquery-search.md">Search</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#index" title="Index">Index</a>: <i>String</i>
<a href="#compute" title="Compute">Compute</a>: <i>
      - <a href="graph-request-logquery-compute.md">Compute</a></i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="graph-request-logquery-groupby.md">GroupBy</a></i>
<a href="#search" title="Search">Search</a>: <i>
      - <a href="graph-request-logquery-search.md">Search</a></i>
</pre>

## Properties

#### Index

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compute

_Required_: No

_Type_: List of <a href="graph-request-logquery-compute.md">Compute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="graph-request-logquery-groupby.md">GroupBy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No

_Type_: List of <a href="graph-request-logquery-search.md">Search</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
