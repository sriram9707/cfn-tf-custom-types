# Terraform::TencentCloud::KubernetesAsScalingGroup AutoScalingConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>" : <i>String</i>,
    "<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>" : <i>Boolean</i>,
    "<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>" : <i>Boolean</i>,
    "<a href="#instancetags" title="InstanceTags">InstanceTags</a>" : <i>[ <a href="autoscalingconfig-instancetags.md">InstanceTags</a>, ... ]</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
    "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
    "<a href="#keyids" title="KeyIds">KeyIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
    "<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>" : <i>Boolean</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
    "<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>" : <i>String</i>,
    "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="autoscalingconfig-datadisk.md">DataDisk</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>: <i>String</i>
<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>: <i>Boolean</i>
<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>: <i>Boolean</i>
<a href="#instancetags" title="InstanceTags">InstanceTags</a>: <i>
      - <a href="autoscalingconfig-instancetags.md">InstanceTags</a></i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
<a href="#keyids" title="KeyIds">KeyIds</a>: <i>
      - String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>: <i>Boolean</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>: <i>String</i>
<a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="autoscalingconfig-datadisk.md">DataDisk</a></i>
</pre>

## Properties

#### ConfigurationName

Name of a launch configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitorService

To specify whether to enable cloud monitor service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedSecurityService

To specify whether to enable cloud security service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTags

A list of tags used to associate different resources.

_Required_: No

_Type_: List of <a href="autoscalingconfig-instancetags.md">InstanceTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Specified types of CVM instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Charge types for network traffic. Available values include `BANDWIDTH_PREPAID`, `TRAFFIC_POSTPAID_BY_HOUR`, `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

Max bandwidth of Internet access in Mbps. Default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIds

ID list of keys.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password to access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Specifys to which project the configuration belongs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAssigned

Specify whether to assign an Internet IP address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

Security groups to which a CVM instance belongs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

Volume of system disk in GB. Default is 50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskType

Type of a CVM disk, and available values include CLOUD_PREMIUM and CLOUD_SSD. Default is CLOUD_PREMIUM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="autoscalingconfig-datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
