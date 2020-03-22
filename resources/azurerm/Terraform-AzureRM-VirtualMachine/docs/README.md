# Terraform::AzureRM::VirtualMachine

Manages a Virtual Machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualMachine",
    "Properties" : {
        "<a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>" : <i>String</i>,
        "<a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>" : <i>Boolean</i>,
        "<a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>" : <i>Boolean</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>" : <i>[ <a href="additionalcapabilities.md">AdditionalCapabilities</a>, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnostics.md">BootDiagnostics</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ <a href="osprofile.md">OsProfile</a>, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a>, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ <a href="osprofilesecrets.md">OsProfileSecrets</a>, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plan.md">Plan</a>, ... ]</i>,
        "<a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>" : <i>[ <a href="storagedatadisk.md">StorageDataDisk</a>, ... ]</i>,
        "<a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>" : <i>[ <a href="storageimagereference.md">StorageImageReference</a>, ... ]</i>,
        "<a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>" : <i>[ <a href="storageosdisk.md">StorageOsDisk</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ <a href="sshkeys.md">SshKeys</a>, ... ]</i>,
        "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ <a href="vaultcertificates.md">VaultCertificates</a>, ... ]</i>,
        "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a>, ... ]</i>,
        "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ <a href="winrm.md">Winrm</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualMachine
Properties:
    <a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>: <i>String</i>
    <a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>: <i>Boolean</i>
    <a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>: <i>Boolean</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>: <i>
      - String</i>
    <a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>: <i>String</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>: <i>
      - <a href="additionalcapabilities.md">AdditionalCapabilities</a></i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnostics.md">BootDiagnostics</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#osprofile" title="OsProfile">OsProfile</a>: <i>
      - <a href="osprofile.md">OsProfile</a></i>
    <a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>: <i>
      - <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a></i>
    <a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>: <i>
      - <a href="osprofilesecrets.md">OsProfileSecrets</a></i>
    <a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>: <i>
      - <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a></i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - <a href="plan.md">Plan</a></i>
    <a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>: <i>
      - <a href="storagedatadisk.md">StorageDataDisk</a></i>
    <a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>: <i>
      - <a href="storageimagereference.md">StorageImageReference</a></i>
    <a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>: <i>
      - <a href="storageosdisk.md">StorageOsDisk</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - <a href="sshkeys.md">SshKeys</a></i>
    <a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - <a href="vaultcertificates.md">VaultCertificates</a></i>
    <a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a></i>
    <a href="#winrm" title="Winrm">Winrm</a>: <i>
      - <a href="winrm.md">Winrm</a></i>
</pre>

## Properties

#### AvailabilitySetId

The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteDataDisksOnTermination

Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOsDiskOnTermination

Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are `Windows_Client` and `Windows_Server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceIds

A list of Network Interface ID's which should be associated with the Virtual Machine.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryNetworkInterfaceId

The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the Virtual Machine.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

Specifies the [size of the Virtual Machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCapabilities

_Required_: No

_Type_: List of <a href="additionalcapabilities.md">AdditionalCapabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of <a href="bootdiagnostics.md">BootDiagnostics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfile

_Required_: No

_Type_: List of <a href="osprofile.md">OsProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileLinuxConfig

_Required_: No

_Type_: List of <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileSecrets

_Required_: No

_Type_: List of <a href="osprofilesecrets.md">OsProfileSecrets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileWindowsConfig

_Required_: No

_Type_: List of <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of <a href="plan.md">Plan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDataDisk

_Required_: No

_Type_: List of <a href="storagedatadisk.md">StorageDataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageImageReference

_Required_: No

_Type_: List of <a href="storageimagereference.md">StorageImageReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageOsDisk

_Required_: No

_Type_: List of <a href="storageosdisk.md">StorageOsDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of <a href="sshkeys.md">SshKeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultCertificates

_Required_: No

_Type_: List of <a href="vaultcertificates.md">VaultCertificates</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No

_Type_: List of <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No

_Type_: List of <a href="winrm.md">Winrm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.
