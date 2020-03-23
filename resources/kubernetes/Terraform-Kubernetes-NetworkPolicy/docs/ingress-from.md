# Terraform::Kubernetes::NetworkPolicy Ingress From

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipblock" title="IpBlock">IpBlock</a>" : <i>[ <a href="ingress-from-ipblock.md">IpBlock</a>, ... ]</i>,
    "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ <a href="ingress-from-namespaceselector.md">NamespaceSelector</a>, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ <a href="ingress-from-podselector.md">PodSelector</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipblock" title="IpBlock">IpBlock</a>: <i>
      - <a href="ingress-from-ipblock.md">IpBlock</a></i>
<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - <a href="ingress-from-namespaceselector.md">NamespaceSelector</a></i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - <a href="ingress-from-podselector.md">PodSelector</a></i>
</pre>

## Properties

#### IpBlock

_Required_: No

_Type_: List of <a href="ingress-from-ipblock.md">IpBlock</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No

_Type_: List of <a href="ingress-from-namespaceselector.md">NamespaceSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No

_Type_: List of <a href="ingress-from-podselector.md">PodSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
