// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/cloudstackserviceaccount.CloudStackServiceAccount has been deprecated in favor of grafana.cloud/stackserviceaccount.StackServiceAccount
type CloudStackServiceAccount struct {
	pulumi.CustomResourceState

	// The disabled status for the service account.
	IsDisabled pulumi.BoolPtrOutput `pulumi:"isDisabled"`
	// The name of the service account.
	Name pulumi.StringOutput `pulumi:"name"`
	// The basic role of the service account in the organization.
	Role      pulumi.StringOutput `pulumi:"role"`
	StackSlug pulumi.StringOutput `pulumi:"stackSlug"`
}

// NewCloudStackServiceAccount registers a new resource with the given unique name, arguments, and options.
func NewCloudStackServiceAccount(ctx *pulumi.Context,
	name string, args *CloudStackServiceAccountArgs, opts ...pulumi.ResourceOption) (*CloudStackServiceAccount, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	if args.StackSlug == nil {
		return nil, errors.New("invalid value for required argument 'StackSlug'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/cloudStackServiceAccount:CloudStackServiceAccount"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CloudStackServiceAccount
	err := ctx.RegisterResource("grafana:index/cloudStackServiceAccount:CloudStackServiceAccount", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCloudStackServiceAccount gets an existing CloudStackServiceAccount resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCloudStackServiceAccount(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CloudStackServiceAccountState, opts ...pulumi.ResourceOption) (*CloudStackServiceAccount, error) {
	var resource CloudStackServiceAccount
	err := ctx.ReadResource("grafana:index/cloudStackServiceAccount:CloudStackServiceAccount", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CloudStackServiceAccount resources.
type cloudStackServiceAccountState struct {
	// The disabled status for the service account.
	IsDisabled *bool `pulumi:"isDisabled"`
	// The name of the service account.
	Name *string `pulumi:"name"`
	// The basic role of the service account in the organization.
	Role      *string `pulumi:"role"`
	StackSlug *string `pulumi:"stackSlug"`
}

type CloudStackServiceAccountState struct {
	// The disabled status for the service account.
	IsDisabled pulumi.BoolPtrInput
	// The name of the service account.
	Name pulumi.StringPtrInput
	// The basic role of the service account in the organization.
	Role      pulumi.StringPtrInput
	StackSlug pulumi.StringPtrInput
}

func (CloudStackServiceAccountState) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudStackServiceAccountState)(nil)).Elem()
}

type cloudStackServiceAccountArgs struct {
	// The disabled status for the service account.
	IsDisabled *bool `pulumi:"isDisabled"`
	// The name of the service account.
	Name *string `pulumi:"name"`
	// The basic role of the service account in the organization.
	Role      string `pulumi:"role"`
	StackSlug string `pulumi:"stackSlug"`
}

// The set of arguments for constructing a CloudStackServiceAccount resource.
type CloudStackServiceAccountArgs struct {
	// The disabled status for the service account.
	IsDisabled pulumi.BoolPtrInput
	// The name of the service account.
	Name pulumi.StringPtrInput
	// The basic role of the service account in the organization.
	Role      pulumi.StringInput
	StackSlug pulumi.StringInput
}

func (CloudStackServiceAccountArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudStackServiceAccountArgs)(nil)).Elem()
}

type CloudStackServiceAccountInput interface {
	pulumi.Input

	ToCloudStackServiceAccountOutput() CloudStackServiceAccountOutput
	ToCloudStackServiceAccountOutputWithContext(ctx context.Context) CloudStackServiceAccountOutput
}

func (*CloudStackServiceAccount) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudStackServiceAccount)(nil)).Elem()
}

func (i *CloudStackServiceAccount) ToCloudStackServiceAccountOutput() CloudStackServiceAccountOutput {
	return i.ToCloudStackServiceAccountOutputWithContext(context.Background())
}

func (i *CloudStackServiceAccount) ToCloudStackServiceAccountOutputWithContext(ctx context.Context) CloudStackServiceAccountOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudStackServiceAccountOutput)
}

// CloudStackServiceAccountArrayInput is an input type that accepts CloudStackServiceAccountArray and CloudStackServiceAccountArrayOutput values.
// You can construct a concrete instance of `CloudStackServiceAccountArrayInput` via:
//
//	CloudStackServiceAccountArray{ CloudStackServiceAccountArgs{...} }
type CloudStackServiceAccountArrayInput interface {
	pulumi.Input

	ToCloudStackServiceAccountArrayOutput() CloudStackServiceAccountArrayOutput
	ToCloudStackServiceAccountArrayOutputWithContext(context.Context) CloudStackServiceAccountArrayOutput
}

type CloudStackServiceAccountArray []CloudStackServiceAccountInput

func (CloudStackServiceAccountArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CloudStackServiceAccount)(nil)).Elem()
}

func (i CloudStackServiceAccountArray) ToCloudStackServiceAccountArrayOutput() CloudStackServiceAccountArrayOutput {
	return i.ToCloudStackServiceAccountArrayOutputWithContext(context.Background())
}

func (i CloudStackServiceAccountArray) ToCloudStackServiceAccountArrayOutputWithContext(ctx context.Context) CloudStackServiceAccountArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudStackServiceAccountArrayOutput)
}

// CloudStackServiceAccountMapInput is an input type that accepts CloudStackServiceAccountMap and CloudStackServiceAccountMapOutput values.
// You can construct a concrete instance of `CloudStackServiceAccountMapInput` via:
//
//	CloudStackServiceAccountMap{ "key": CloudStackServiceAccountArgs{...} }
type CloudStackServiceAccountMapInput interface {
	pulumi.Input

	ToCloudStackServiceAccountMapOutput() CloudStackServiceAccountMapOutput
	ToCloudStackServiceAccountMapOutputWithContext(context.Context) CloudStackServiceAccountMapOutput
}

type CloudStackServiceAccountMap map[string]CloudStackServiceAccountInput

func (CloudStackServiceAccountMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CloudStackServiceAccount)(nil)).Elem()
}

func (i CloudStackServiceAccountMap) ToCloudStackServiceAccountMapOutput() CloudStackServiceAccountMapOutput {
	return i.ToCloudStackServiceAccountMapOutputWithContext(context.Background())
}

func (i CloudStackServiceAccountMap) ToCloudStackServiceAccountMapOutputWithContext(ctx context.Context) CloudStackServiceAccountMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudStackServiceAccountMapOutput)
}

type CloudStackServiceAccountOutput struct{ *pulumi.OutputState }

func (CloudStackServiceAccountOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudStackServiceAccount)(nil)).Elem()
}

func (o CloudStackServiceAccountOutput) ToCloudStackServiceAccountOutput() CloudStackServiceAccountOutput {
	return o
}

func (o CloudStackServiceAccountOutput) ToCloudStackServiceAccountOutputWithContext(ctx context.Context) CloudStackServiceAccountOutput {
	return o
}

// The disabled status for the service account.
func (o CloudStackServiceAccountOutput) IsDisabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *CloudStackServiceAccount) pulumi.BoolPtrOutput { return v.IsDisabled }).(pulumi.BoolPtrOutput)
}

// The name of the service account.
func (o CloudStackServiceAccountOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudStackServiceAccount) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The basic role of the service account in the organization.
func (o CloudStackServiceAccountOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudStackServiceAccount) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

func (o CloudStackServiceAccountOutput) StackSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudStackServiceAccount) pulumi.StringOutput { return v.StackSlug }).(pulumi.StringOutput)
}

type CloudStackServiceAccountArrayOutput struct{ *pulumi.OutputState }

func (CloudStackServiceAccountArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CloudStackServiceAccount)(nil)).Elem()
}

func (o CloudStackServiceAccountArrayOutput) ToCloudStackServiceAccountArrayOutput() CloudStackServiceAccountArrayOutput {
	return o
}

func (o CloudStackServiceAccountArrayOutput) ToCloudStackServiceAccountArrayOutputWithContext(ctx context.Context) CloudStackServiceAccountArrayOutput {
	return o
}

func (o CloudStackServiceAccountArrayOutput) Index(i pulumi.IntInput) CloudStackServiceAccountOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CloudStackServiceAccount {
		return vs[0].([]*CloudStackServiceAccount)[vs[1].(int)]
	}).(CloudStackServiceAccountOutput)
}

type CloudStackServiceAccountMapOutput struct{ *pulumi.OutputState }

func (CloudStackServiceAccountMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CloudStackServiceAccount)(nil)).Elem()
}

func (o CloudStackServiceAccountMapOutput) ToCloudStackServiceAccountMapOutput() CloudStackServiceAccountMapOutput {
	return o
}

func (o CloudStackServiceAccountMapOutput) ToCloudStackServiceAccountMapOutputWithContext(ctx context.Context) CloudStackServiceAccountMapOutput {
	return o
}

func (o CloudStackServiceAccountMapOutput) MapIndex(k pulumi.StringInput) CloudStackServiceAccountOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CloudStackServiceAccount {
		return vs[0].(map[string]*CloudStackServiceAccount)[vs[1].(string)]
	}).(CloudStackServiceAccountOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CloudStackServiceAccountInput)(nil)).Elem(), &CloudStackServiceAccount{})
	pulumi.RegisterInputType(reflect.TypeOf((*CloudStackServiceAccountArrayInput)(nil)).Elem(), CloudStackServiceAccountArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CloudStackServiceAccountMapInput)(nil)).Elem(), CloudStackServiceAccountMap{})
	pulumi.RegisterOutputType(CloudStackServiceAccountOutput{})
	pulumi.RegisterOutputType(CloudStackServiceAccountArrayOutput{})
	pulumi.RegisterOutputType(CloudStackServiceAccountMapOutput{})
}
