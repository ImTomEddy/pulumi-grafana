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

type SyntheticMonitoringProbe struct {
	pulumi.CustomResourceState

	// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
	AuthToken pulumi.StringOutput `pulumi:"authToken"`
	// Custom labels to be included with collected metrics and logs.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// Latitude coordinates.
	Latitude pulumi.Float64Output `pulumi:"latitude"`
	// Longitude coordinates.
	Longitude pulumi.Float64Output `pulumi:"longitude"`
	// Name of the probe.
	Name pulumi.StringOutput `pulumi:"name"`
	// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
	// to `true`.
	Public pulumi.BoolPtrOutput `pulumi:"public"`
	// Region of the probe.
	Region pulumi.StringOutput `pulumi:"region"`
	// The tenant ID of the probe.
	TenantId pulumi.IntOutput `pulumi:"tenantId"`
}

// NewSyntheticMonitoringProbe registers a new resource with the given unique name, arguments, and options.
func NewSyntheticMonitoringProbe(ctx *pulumi.Context,
	name string, args *SyntheticMonitoringProbeArgs, opts ...pulumi.ResourceOption) (*SyntheticMonitoringProbe, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Latitude == nil {
		return nil, errors.New("invalid value for required argument 'Latitude'")
	}
	if args.Longitude == nil {
		return nil, errors.New("invalid value for required argument 'Longitude'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"authToken",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SyntheticMonitoringProbe
	err := ctx.RegisterResource("grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSyntheticMonitoringProbe gets an existing SyntheticMonitoringProbe resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSyntheticMonitoringProbe(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SyntheticMonitoringProbeState, opts ...pulumi.ResourceOption) (*SyntheticMonitoringProbe, error) {
	var resource SyntheticMonitoringProbe
	err := ctx.ReadResource("grafana:index/syntheticMonitoringProbe:SyntheticMonitoringProbe", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SyntheticMonitoringProbe resources.
type syntheticMonitoringProbeState struct {
	// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
	AuthToken *string `pulumi:"authToken"`
	// Custom labels to be included with collected metrics and logs.
	Labels map[string]string `pulumi:"labels"`
	// Latitude coordinates.
	Latitude *float64 `pulumi:"latitude"`
	// Longitude coordinates.
	Longitude *float64 `pulumi:"longitude"`
	// Name of the probe.
	Name *string `pulumi:"name"`
	// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
	// to `true`.
	Public *bool `pulumi:"public"`
	// Region of the probe.
	Region *string `pulumi:"region"`
	// The tenant ID of the probe.
	TenantId *int `pulumi:"tenantId"`
}

type SyntheticMonitoringProbeState struct {
	// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
	AuthToken pulumi.StringPtrInput
	// Custom labels to be included with collected metrics and logs.
	Labels pulumi.StringMapInput
	// Latitude coordinates.
	Latitude pulumi.Float64PtrInput
	// Longitude coordinates.
	Longitude pulumi.Float64PtrInput
	// Name of the probe.
	Name pulumi.StringPtrInput
	// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
	// to `true`.
	Public pulumi.BoolPtrInput
	// Region of the probe.
	Region pulumi.StringPtrInput
	// The tenant ID of the probe.
	TenantId pulumi.IntPtrInput
}

func (SyntheticMonitoringProbeState) ElementType() reflect.Type {
	return reflect.TypeOf((*syntheticMonitoringProbeState)(nil)).Elem()
}

type syntheticMonitoringProbeArgs struct {
	// Custom labels to be included with collected metrics and logs.
	Labels map[string]string `pulumi:"labels"`
	// Latitude coordinates.
	Latitude float64 `pulumi:"latitude"`
	// Longitude coordinates.
	Longitude float64 `pulumi:"longitude"`
	// Name of the probe.
	Name *string `pulumi:"name"`
	// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
	// to `true`.
	Public *bool `pulumi:"public"`
	// Region of the probe.
	Region string `pulumi:"region"`
}

// The set of arguments for constructing a SyntheticMonitoringProbe resource.
type SyntheticMonitoringProbeArgs struct {
	// Custom labels to be included with collected metrics and logs.
	Labels pulumi.StringMapInput
	// Latitude coordinates.
	Latitude pulumi.Float64Input
	// Longitude coordinates.
	Longitude pulumi.Float64Input
	// Name of the probe.
	Name pulumi.StringPtrInput
	// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
	// to `true`.
	Public pulumi.BoolPtrInput
	// Region of the probe.
	Region pulumi.StringInput
}

func (SyntheticMonitoringProbeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*syntheticMonitoringProbeArgs)(nil)).Elem()
}

type SyntheticMonitoringProbeInput interface {
	pulumi.Input

	ToSyntheticMonitoringProbeOutput() SyntheticMonitoringProbeOutput
	ToSyntheticMonitoringProbeOutputWithContext(ctx context.Context) SyntheticMonitoringProbeOutput
}

func (*SyntheticMonitoringProbe) ElementType() reflect.Type {
	return reflect.TypeOf((**SyntheticMonitoringProbe)(nil)).Elem()
}

func (i *SyntheticMonitoringProbe) ToSyntheticMonitoringProbeOutput() SyntheticMonitoringProbeOutput {
	return i.ToSyntheticMonitoringProbeOutputWithContext(context.Background())
}

func (i *SyntheticMonitoringProbe) ToSyntheticMonitoringProbeOutputWithContext(ctx context.Context) SyntheticMonitoringProbeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringProbeOutput)
}

// SyntheticMonitoringProbeArrayInput is an input type that accepts SyntheticMonitoringProbeArray and SyntheticMonitoringProbeArrayOutput values.
// You can construct a concrete instance of `SyntheticMonitoringProbeArrayInput` via:
//
//	SyntheticMonitoringProbeArray{ SyntheticMonitoringProbeArgs{...} }
type SyntheticMonitoringProbeArrayInput interface {
	pulumi.Input

	ToSyntheticMonitoringProbeArrayOutput() SyntheticMonitoringProbeArrayOutput
	ToSyntheticMonitoringProbeArrayOutputWithContext(context.Context) SyntheticMonitoringProbeArrayOutput
}

type SyntheticMonitoringProbeArray []SyntheticMonitoringProbeInput

func (SyntheticMonitoringProbeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SyntheticMonitoringProbe)(nil)).Elem()
}

func (i SyntheticMonitoringProbeArray) ToSyntheticMonitoringProbeArrayOutput() SyntheticMonitoringProbeArrayOutput {
	return i.ToSyntheticMonitoringProbeArrayOutputWithContext(context.Background())
}

func (i SyntheticMonitoringProbeArray) ToSyntheticMonitoringProbeArrayOutputWithContext(ctx context.Context) SyntheticMonitoringProbeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringProbeArrayOutput)
}

// SyntheticMonitoringProbeMapInput is an input type that accepts SyntheticMonitoringProbeMap and SyntheticMonitoringProbeMapOutput values.
// You can construct a concrete instance of `SyntheticMonitoringProbeMapInput` via:
//
//	SyntheticMonitoringProbeMap{ "key": SyntheticMonitoringProbeArgs{...} }
type SyntheticMonitoringProbeMapInput interface {
	pulumi.Input

	ToSyntheticMonitoringProbeMapOutput() SyntheticMonitoringProbeMapOutput
	ToSyntheticMonitoringProbeMapOutputWithContext(context.Context) SyntheticMonitoringProbeMapOutput
}

type SyntheticMonitoringProbeMap map[string]SyntheticMonitoringProbeInput

func (SyntheticMonitoringProbeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SyntheticMonitoringProbe)(nil)).Elem()
}

func (i SyntheticMonitoringProbeMap) ToSyntheticMonitoringProbeMapOutput() SyntheticMonitoringProbeMapOutput {
	return i.ToSyntheticMonitoringProbeMapOutputWithContext(context.Background())
}

func (i SyntheticMonitoringProbeMap) ToSyntheticMonitoringProbeMapOutputWithContext(ctx context.Context) SyntheticMonitoringProbeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringProbeMapOutput)
}

type SyntheticMonitoringProbeOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringProbeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SyntheticMonitoringProbe)(nil)).Elem()
}

func (o SyntheticMonitoringProbeOutput) ToSyntheticMonitoringProbeOutput() SyntheticMonitoringProbeOutput {
	return o
}

func (o SyntheticMonitoringProbeOutput) ToSyntheticMonitoringProbeOutputWithContext(ctx context.Context) SyntheticMonitoringProbeOutput {
	return o
}

// The probe authentication token. Your probe must use this to authenticate with Grafana Cloud.
func (o SyntheticMonitoringProbeOutput) AuthToken() pulumi.StringOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.StringOutput { return v.AuthToken }).(pulumi.StringOutput)
}

// Custom labels to be included with collected metrics and logs.
func (o SyntheticMonitoringProbeOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// Latitude coordinates.
func (o SyntheticMonitoringProbeOutput) Latitude() pulumi.Float64Output {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.Float64Output { return v.Latitude }).(pulumi.Float64Output)
}

// Longitude coordinates.
func (o SyntheticMonitoringProbeOutput) Longitude() pulumi.Float64Output {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.Float64Output { return v.Longitude }).(pulumi.Float64Output)
}

// Name of the probe.
func (o SyntheticMonitoringProbeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Public probes are run by Grafana Labs and can be used by all users. Only Grafana Labs managed public probes will be set
// to `true`.
func (o SyntheticMonitoringProbeOutput) Public() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.BoolPtrOutput { return v.Public }).(pulumi.BoolPtrOutput)
}

// Region of the probe.
func (o SyntheticMonitoringProbeOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// The tenant ID of the probe.
func (o SyntheticMonitoringProbeOutput) TenantId() pulumi.IntOutput {
	return o.ApplyT(func(v *SyntheticMonitoringProbe) pulumi.IntOutput { return v.TenantId }).(pulumi.IntOutput)
}

type SyntheticMonitoringProbeArrayOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringProbeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SyntheticMonitoringProbe)(nil)).Elem()
}

func (o SyntheticMonitoringProbeArrayOutput) ToSyntheticMonitoringProbeArrayOutput() SyntheticMonitoringProbeArrayOutput {
	return o
}

func (o SyntheticMonitoringProbeArrayOutput) ToSyntheticMonitoringProbeArrayOutputWithContext(ctx context.Context) SyntheticMonitoringProbeArrayOutput {
	return o
}

func (o SyntheticMonitoringProbeArrayOutput) Index(i pulumi.IntInput) SyntheticMonitoringProbeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SyntheticMonitoringProbe {
		return vs[0].([]*SyntheticMonitoringProbe)[vs[1].(int)]
	}).(SyntheticMonitoringProbeOutput)
}

type SyntheticMonitoringProbeMapOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringProbeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SyntheticMonitoringProbe)(nil)).Elem()
}

func (o SyntheticMonitoringProbeMapOutput) ToSyntheticMonitoringProbeMapOutput() SyntheticMonitoringProbeMapOutput {
	return o
}

func (o SyntheticMonitoringProbeMapOutput) ToSyntheticMonitoringProbeMapOutputWithContext(ctx context.Context) SyntheticMonitoringProbeMapOutput {
	return o
}

func (o SyntheticMonitoringProbeMapOutput) MapIndex(k pulumi.StringInput) SyntheticMonitoringProbeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SyntheticMonitoringProbe {
		return vs[0].(map[string]*SyntheticMonitoringProbe)[vs[1].(string)]
	}).(SyntheticMonitoringProbeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringProbeInput)(nil)).Elem(), &SyntheticMonitoringProbe{})
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringProbeArrayInput)(nil)).Elem(), SyntheticMonitoringProbeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringProbeMapInput)(nil)).Elem(), SyntheticMonitoringProbeMap{})
	pulumi.RegisterOutputType(SyntheticMonitoringProbeOutput{})
	pulumi.RegisterOutputType(SyntheticMonitoringProbeArrayOutput{})
	pulumi.RegisterOutputType(SyntheticMonitoringProbeMapOutput{})
}
