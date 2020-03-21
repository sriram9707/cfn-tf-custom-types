# Terraform::Kubernetes::CronJob JobTemplate Spec DnsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameservers" title="Nameservers">Nameservers</a>" : <i>[ String, ... ]</i>,
    "<a href="#searches" title="Searches">Searches</a>" : <i>[ String, ... ]</i>,
    "<a href="#option" title="Option">Option</a>" : <i>[ <a href="jobtemplate-spec-dnsconfig-option.md">Option</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameservers" title="Nameservers">Nameservers</a>: <i>
      - String</i>
<a href="#searches" title="Searches">Searches</a>: <i>
      - String</i>
<a href="#option" title="Option">Option</a>: <i>
      - <a href="jobtemplate-spec-dnsconfig-option.md">Option</a></i>
</pre>

## Properties

#### Nameservers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Searches

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of <a href="jobtemplate-spec-dnsconfig-option.md">Option</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
