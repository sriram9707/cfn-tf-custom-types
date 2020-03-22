# Terraform::Google::ComputeInstanceFromTemplate Scheduling

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automaticrestart" title="AutomaticRestart">AutomaticRestart</a>" : <i>Boolean</i>,
    "<a href="#onhostmaintenance" title="OnHostMaintenance">OnHostMaintenance</a>" : <i>String</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>" : <i>[ <a href="scheduling-nodeaffinities.md">NodeAffinities</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automaticrestart" title="AutomaticRestart">AutomaticRestart</a>: <i>Boolean</i>
<a href="#onhostmaintenance" title="OnHostMaintenance">OnHostMaintenance</a>: <i>String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>: <i>
      - <a href="scheduling-nodeaffinities.md">NodeAffinities</a></i>
</pre>

## Properties

#### AutomaticRestart

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnHostMaintenance

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinities

_Required_: No

_Type_: List of <a href="scheduling-nodeaffinities.md">NodeAffinities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
