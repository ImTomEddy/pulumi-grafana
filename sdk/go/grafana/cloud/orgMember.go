// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloud

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Manages the membership of a user in an organization.
//
// ## Import
//
// ```sh
// $ pulumi import grafana:cloud/orgMember:OrgMember name "{{ orgSlugOrID }}:{{ usernameOrID }}"
// ```
type OrgMember struct {
	pulumi.CustomResourceState

	// The slug or ID of the organization.
	Org pulumi.StringOutput `pulumi:"org"`
	// Whether the user should receive billing emails.
	ReceiveBillingEmails pulumi.BoolOutput `pulumi:"receiveBillingEmails"`
	// The role to assign to the user in the organization.
	Role pulumi.StringOutput `pulumi:"role"`
	// Username or ID of the user to add to the org's members.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewOrgMember registers a new resource with the given unique name, arguments, and options.
func NewOrgMember(ctx *pulumi.Context,
	name string, args *OrgMemberArgs, opts ...pulumi.ResourceOption) (*OrgMember, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Org == nil {
		return nil, errors.New("invalid value for required argument 'Org'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/cloudOrgMember:CloudOrgMember"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrgMember
	err := ctx.RegisterResource("grafana:cloud/orgMember:OrgMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrgMember gets an existing OrgMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrgMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrgMemberState, opts ...pulumi.ResourceOption) (*OrgMember, error) {
	var resource OrgMember
	err := ctx.ReadResource("grafana:cloud/orgMember:OrgMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrgMember resources.
type orgMemberState struct {
	// The slug or ID of the organization.
	Org *string `pulumi:"org"`
	// Whether the user should receive billing emails.
	ReceiveBillingEmails *bool `pulumi:"receiveBillingEmails"`
	// The role to assign to the user in the organization.
	Role *string `pulumi:"role"`
	// Username or ID of the user to add to the org's members.
	User *string `pulumi:"user"`
}

type OrgMemberState struct {
	// The slug or ID of the organization.
	Org pulumi.StringPtrInput
	// Whether the user should receive billing emails.
	ReceiveBillingEmails pulumi.BoolPtrInput
	// The role to assign to the user in the organization.
	Role pulumi.StringPtrInput
	// Username or ID of the user to add to the org's members.
	User pulumi.StringPtrInput
}

func (OrgMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*orgMemberState)(nil)).Elem()
}

type orgMemberArgs struct {
	// The slug or ID of the organization.
	Org string `pulumi:"org"`
	// Whether the user should receive billing emails.
	ReceiveBillingEmails *bool `pulumi:"receiveBillingEmails"`
	// The role to assign to the user in the organization.
	Role string `pulumi:"role"`
	// Username or ID of the user to add to the org's members.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a OrgMember resource.
type OrgMemberArgs struct {
	// The slug or ID of the organization.
	Org pulumi.StringInput
	// Whether the user should receive billing emails.
	ReceiveBillingEmails pulumi.BoolPtrInput
	// The role to assign to the user in the organization.
	Role pulumi.StringInput
	// Username or ID of the user to add to the org's members.
	User pulumi.StringInput
}

func (OrgMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*orgMemberArgs)(nil)).Elem()
}

type OrgMemberInput interface {
	pulumi.Input

	ToOrgMemberOutput() OrgMemberOutput
	ToOrgMemberOutputWithContext(ctx context.Context) OrgMemberOutput
}

func (*OrgMember) ElementType() reflect.Type {
	return reflect.TypeOf((**OrgMember)(nil)).Elem()
}

func (i *OrgMember) ToOrgMemberOutput() OrgMemberOutput {
	return i.ToOrgMemberOutputWithContext(context.Background())
}

func (i *OrgMember) ToOrgMemberOutputWithContext(ctx context.Context) OrgMemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgMemberOutput)
}

// OrgMemberArrayInput is an input type that accepts OrgMemberArray and OrgMemberArrayOutput values.
// You can construct a concrete instance of `OrgMemberArrayInput` via:
//
//	OrgMemberArray{ OrgMemberArgs{...} }
type OrgMemberArrayInput interface {
	pulumi.Input

	ToOrgMemberArrayOutput() OrgMemberArrayOutput
	ToOrgMemberArrayOutputWithContext(context.Context) OrgMemberArrayOutput
}

type OrgMemberArray []OrgMemberInput

func (OrgMemberArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrgMember)(nil)).Elem()
}

func (i OrgMemberArray) ToOrgMemberArrayOutput() OrgMemberArrayOutput {
	return i.ToOrgMemberArrayOutputWithContext(context.Background())
}

func (i OrgMemberArray) ToOrgMemberArrayOutputWithContext(ctx context.Context) OrgMemberArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgMemberArrayOutput)
}

// OrgMemberMapInput is an input type that accepts OrgMemberMap and OrgMemberMapOutput values.
// You can construct a concrete instance of `OrgMemberMapInput` via:
//
//	OrgMemberMap{ "key": OrgMemberArgs{...} }
type OrgMemberMapInput interface {
	pulumi.Input

	ToOrgMemberMapOutput() OrgMemberMapOutput
	ToOrgMemberMapOutputWithContext(context.Context) OrgMemberMapOutput
}

type OrgMemberMap map[string]OrgMemberInput

func (OrgMemberMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrgMember)(nil)).Elem()
}

func (i OrgMemberMap) ToOrgMemberMapOutput() OrgMemberMapOutput {
	return i.ToOrgMemberMapOutputWithContext(context.Background())
}

func (i OrgMemberMap) ToOrgMemberMapOutputWithContext(ctx context.Context) OrgMemberMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgMemberMapOutput)
}

type OrgMemberOutput struct{ *pulumi.OutputState }

func (OrgMemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrgMember)(nil)).Elem()
}

func (o OrgMemberOutput) ToOrgMemberOutput() OrgMemberOutput {
	return o
}

func (o OrgMemberOutput) ToOrgMemberOutputWithContext(ctx context.Context) OrgMemberOutput {
	return o
}

// The slug or ID of the organization.
func (o OrgMemberOutput) Org() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgMember) pulumi.StringOutput { return v.Org }).(pulumi.StringOutput)
}

// Whether the user should receive billing emails.
func (o OrgMemberOutput) ReceiveBillingEmails() pulumi.BoolOutput {
	return o.ApplyT(func(v *OrgMember) pulumi.BoolOutput { return v.ReceiveBillingEmails }).(pulumi.BoolOutput)
}

// The role to assign to the user in the organization.
func (o OrgMemberOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgMember) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

// Username or ID of the user to add to the org's members.
func (o OrgMemberOutput) User() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgMember) pulumi.StringOutput { return v.User }).(pulumi.StringOutput)
}

type OrgMemberArrayOutput struct{ *pulumi.OutputState }

func (OrgMemberArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrgMember)(nil)).Elem()
}

func (o OrgMemberArrayOutput) ToOrgMemberArrayOutput() OrgMemberArrayOutput {
	return o
}

func (o OrgMemberArrayOutput) ToOrgMemberArrayOutputWithContext(ctx context.Context) OrgMemberArrayOutput {
	return o
}

func (o OrgMemberArrayOutput) Index(i pulumi.IntInput) OrgMemberOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OrgMember {
		return vs[0].([]*OrgMember)[vs[1].(int)]
	}).(OrgMemberOutput)
}

type OrgMemberMapOutput struct{ *pulumi.OutputState }

func (OrgMemberMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrgMember)(nil)).Elem()
}

func (o OrgMemberMapOutput) ToOrgMemberMapOutput() OrgMemberMapOutput {
	return o
}

func (o OrgMemberMapOutput) ToOrgMemberMapOutputWithContext(ctx context.Context) OrgMemberMapOutput {
	return o
}

func (o OrgMemberMapOutput) MapIndex(k pulumi.StringInput) OrgMemberOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OrgMember {
		return vs[0].(map[string]*OrgMember)[vs[1].(string)]
	}).(OrgMemberOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrgMemberInput)(nil)).Elem(), &OrgMember{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrgMemberArrayInput)(nil)).Elem(), OrgMemberArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrgMemberMapInput)(nil)).Elem(), OrgMemberMap{})
	pulumi.RegisterOutputType(OrgMemberOutput{})
	pulumi.RegisterOutputType(OrgMemberArrayOutput{})
	pulumi.RegisterOutputType(OrgMemberMapOutput{})
}