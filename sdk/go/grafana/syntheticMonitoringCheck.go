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

type SyntheticMonitoringCheck struct {
	pulumi.CustomResourceState

	// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
	// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
	AlertSensitivity pulumi.StringPtrOutput `pulumi:"alertSensitivity"`
	// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
	// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
	BasicMetricsOnly pulumi.BoolPtrOutput `pulumi:"basicMetricsOnly"`
	// Whether to enable the check.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
	// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
	Frequency pulumi.IntPtrOutput `pulumi:"frequency"`
	// Name used for job label.
	Job pulumi.StringOutput `pulumi:"job"`
	// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
	// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
	// the labels cannot be empty, and the maximum length is 32 bytes.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// List of probe location IDs where this target will be checked from.
	Probes pulumi.IntArrayOutput `pulumi:"probes"`
	// Check settings. Should contain exactly one nested block.
	Settings SyntheticMonitoringCheckSettingsOutput `pulumi:"settings"`
	// Hostname to ping.
	Target pulumi.StringOutput `pulumi:"target"`
	// The tenant ID of the check.
	TenantId pulumi.IntOutput `pulumi:"tenantId"`
	// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
	// and the maximum 10 seconds (10000 ms).
	Timeout pulumi.IntPtrOutput `pulumi:"timeout"`
}

// NewSyntheticMonitoringCheck registers a new resource with the given unique name, arguments, and options.
func NewSyntheticMonitoringCheck(ctx *pulumi.Context,
	name string, args *SyntheticMonitoringCheckArgs, opts ...pulumi.ResourceOption) (*SyntheticMonitoringCheck, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Job == nil {
		return nil, errors.New("invalid value for required argument 'Job'")
	}
	if args.Probes == nil {
		return nil, errors.New("invalid value for required argument 'Probes'")
	}
	if args.Settings == nil {
		return nil, errors.New("invalid value for required argument 'Settings'")
	}
	if args.Target == nil {
		return nil, errors.New("invalid value for required argument 'Target'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SyntheticMonitoringCheck
	err := ctx.RegisterResource("grafana:index/syntheticMonitoringCheck:SyntheticMonitoringCheck", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSyntheticMonitoringCheck gets an existing SyntheticMonitoringCheck resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSyntheticMonitoringCheck(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SyntheticMonitoringCheckState, opts ...pulumi.ResourceOption) (*SyntheticMonitoringCheck, error) {
	var resource SyntheticMonitoringCheck
	err := ctx.ReadResource("grafana:index/syntheticMonitoringCheck:SyntheticMonitoringCheck", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SyntheticMonitoringCheck resources.
type syntheticMonitoringCheckState struct {
	// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
	// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
	AlertSensitivity *string `pulumi:"alertSensitivity"`
	// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
	// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
	BasicMetricsOnly *bool `pulumi:"basicMetricsOnly"`
	// Whether to enable the check.
	Enabled *bool `pulumi:"enabled"`
	// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
	// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
	Frequency *int `pulumi:"frequency"`
	// Name used for job label.
	Job *string `pulumi:"job"`
	// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
	// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
	// the labels cannot be empty, and the maximum length is 32 bytes.
	Labels map[string]string `pulumi:"labels"`
	// List of probe location IDs where this target will be checked from.
	Probes []int `pulumi:"probes"`
	// Check settings. Should contain exactly one nested block.
	Settings *SyntheticMonitoringCheckSettings `pulumi:"settings"`
	// Hostname to ping.
	Target *string `pulumi:"target"`
	// The tenant ID of the check.
	TenantId *int `pulumi:"tenantId"`
	// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
	// and the maximum 10 seconds (10000 ms).
	Timeout *int `pulumi:"timeout"`
}

type SyntheticMonitoringCheckState struct {
	// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
	// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
	AlertSensitivity pulumi.StringPtrInput
	// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
	// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
	BasicMetricsOnly pulumi.BoolPtrInput
	// Whether to enable the check.
	Enabled pulumi.BoolPtrInput
	// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
	// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
	Frequency pulumi.IntPtrInput
	// Name used for job label.
	Job pulumi.StringPtrInput
	// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
	// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
	// the labels cannot be empty, and the maximum length is 32 bytes.
	Labels pulumi.StringMapInput
	// List of probe location IDs where this target will be checked from.
	Probes pulumi.IntArrayInput
	// Check settings. Should contain exactly one nested block.
	Settings SyntheticMonitoringCheckSettingsPtrInput
	// Hostname to ping.
	Target pulumi.StringPtrInput
	// The tenant ID of the check.
	TenantId pulumi.IntPtrInput
	// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
	// and the maximum 10 seconds (10000 ms).
	Timeout pulumi.IntPtrInput
}

func (SyntheticMonitoringCheckState) ElementType() reflect.Type {
	return reflect.TypeOf((*syntheticMonitoringCheckState)(nil)).Elem()
}

type syntheticMonitoringCheckArgs struct {
	// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
	// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
	AlertSensitivity *string `pulumi:"alertSensitivity"`
	// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
	// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
	BasicMetricsOnly *bool `pulumi:"basicMetricsOnly"`
	// Whether to enable the check.
	Enabled *bool `pulumi:"enabled"`
	// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
	// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
	Frequency *int `pulumi:"frequency"`
	// Name used for job label.
	Job string `pulumi:"job"`
	// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
	// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
	// the labels cannot be empty, and the maximum length is 32 bytes.
	Labels map[string]string `pulumi:"labels"`
	// List of probe location IDs where this target will be checked from.
	Probes []int `pulumi:"probes"`
	// Check settings. Should contain exactly one nested block.
	Settings SyntheticMonitoringCheckSettings `pulumi:"settings"`
	// Hostname to ping.
	Target string `pulumi:"target"`
	// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
	// and the maximum 10 seconds (10000 ms).
	Timeout *int `pulumi:"timeout"`
}

// The set of arguments for constructing a SyntheticMonitoringCheck resource.
type SyntheticMonitoringCheckArgs struct {
	// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
	// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
	AlertSensitivity pulumi.StringPtrInput
	// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
	// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
	BasicMetricsOnly pulumi.BoolPtrInput
	// Whether to enable the check.
	Enabled pulumi.BoolPtrInput
	// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
	// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
	Frequency pulumi.IntPtrInput
	// Name used for job label.
	Job pulumi.StringInput
	// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
	// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
	// the labels cannot be empty, and the maximum length is 32 bytes.
	Labels pulumi.StringMapInput
	// List of probe location IDs where this target will be checked from.
	Probes pulumi.IntArrayInput
	// Check settings. Should contain exactly one nested block.
	Settings SyntheticMonitoringCheckSettingsInput
	// Hostname to ping.
	Target pulumi.StringInput
	// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
	// and the maximum 10 seconds (10000 ms).
	Timeout pulumi.IntPtrInput
}

func (SyntheticMonitoringCheckArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*syntheticMonitoringCheckArgs)(nil)).Elem()
}

type SyntheticMonitoringCheckInput interface {
	pulumi.Input

	ToSyntheticMonitoringCheckOutput() SyntheticMonitoringCheckOutput
	ToSyntheticMonitoringCheckOutputWithContext(ctx context.Context) SyntheticMonitoringCheckOutput
}

func (*SyntheticMonitoringCheck) ElementType() reflect.Type {
	return reflect.TypeOf((**SyntheticMonitoringCheck)(nil)).Elem()
}

func (i *SyntheticMonitoringCheck) ToSyntheticMonitoringCheckOutput() SyntheticMonitoringCheckOutput {
	return i.ToSyntheticMonitoringCheckOutputWithContext(context.Background())
}

func (i *SyntheticMonitoringCheck) ToSyntheticMonitoringCheckOutputWithContext(ctx context.Context) SyntheticMonitoringCheckOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringCheckOutput)
}

// SyntheticMonitoringCheckArrayInput is an input type that accepts SyntheticMonitoringCheckArray and SyntheticMonitoringCheckArrayOutput values.
// You can construct a concrete instance of `SyntheticMonitoringCheckArrayInput` via:
//
//	SyntheticMonitoringCheckArray{ SyntheticMonitoringCheckArgs{...} }
type SyntheticMonitoringCheckArrayInput interface {
	pulumi.Input

	ToSyntheticMonitoringCheckArrayOutput() SyntheticMonitoringCheckArrayOutput
	ToSyntheticMonitoringCheckArrayOutputWithContext(context.Context) SyntheticMonitoringCheckArrayOutput
}

type SyntheticMonitoringCheckArray []SyntheticMonitoringCheckInput

func (SyntheticMonitoringCheckArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SyntheticMonitoringCheck)(nil)).Elem()
}

func (i SyntheticMonitoringCheckArray) ToSyntheticMonitoringCheckArrayOutput() SyntheticMonitoringCheckArrayOutput {
	return i.ToSyntheticMonitoringCheckArrayOutputWithContext(context.Background())
}

func (i SyntheticMonitoringCheckArray) ToSyntheticMonitoringCheckArrayOutputWithContext(ctx context.Context) SyntheticMonitoringCheckArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringCheckArrayOutput)
}

// SyntheticMonitoringCheckMapInput is an input type that accepts SyntheticMonitoringCheckMap and SyntheticMonitoringCheckMapOutput values.
// You can construct a concrete instance of `SyntheticMonitoringCheckMapInput` via:
//
//	SyntheticMonitoringCheckMap{ "key": SyntheticMonitoringCheckArgs{...} }
type SyntheticMonitoringCheckMapInput interface {
	pulumi.Input

	ToSyntheticMonitoringCheckMapOutput() SyntheticMonitoringCheckMapOutput
	ToSyntheticMonitoringCheckMapOutputWithContext(context.Context) SyntheticMonitoringCheckMapOutput
}

type SyntheticMonitoringCheckMap map[string]SyntheticMonitoringCheckInput

func (SyntheticMonitoringCheckMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SyntheticMonitoringCheck)(nil)).Elem()
}

func (i SyntheticMonitoringCheckMap) ToSyntheticMonitoringCheckMapOutput() SyntheticMonitoringCheckMapOutput {
	return i.ToSyntheticMonitoringCheckMapOutputWithContext(context.Background())
}

func (i SyntheticMonitoringCheckMap) ToSyntheticMonitoringCheckMapOutputWithContext(ctx context.Context) SyntheticMonitoringCheckMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SyntheticMonitoringCheckMapOutput)
}

type SyntheticMonitoringCheckOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringCheckOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SyntheticMonitoringCheck)(nil)).Elem()
}

func (o SyntheticMonitoringCheckOutput) ToSyntheticMonitoringCheckOutput() SyntheticMonitoringCheckOutput {
	return o
}

func (o SyntheticMonitoringCheckOutput) ToSyntheticMonitoringCheckOutputWithContext(ctx context.Context) SyntheticMonitoringCheckOutput {
	return o
}

// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert
// levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/).
func (o SyntheticMonitoringCheckOutput) AlertSensitivity() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.StringPtrOutput { return v.AlertSensitivity }).(pulumi.StringPtrOutput)
}

// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of
// metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each.
func (o SyntheticMonitoringCheckOutput) BasicMetricsOnly() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.BoolPtrOutput { return v.BasicMetricsOnly }).(pulumi.BoolPtrOutput)
}

// Whether to enable the check.
func (o SyntheticMonitoringCheckOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable
// value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms).
func (o SyntheticMonitoringCheckOutput) Frequency() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.IntPtrOutput { return v.Frequency }).(pulumi.IntPtrOutput)
}

// Name used for job label.
func (o SyntheticMonitoringCheckOutput) Job() pulumi.StringOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.StringOutput { return v.Job }).(pulumi.StringOutput)
}

// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per
// check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of
// the labels cannot be empty, and the maximum length is 32 bytes.
func (o SyntheticMonitoringCheckOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// List of probe location IDs where this target will be checked from.
func (o SyntheticMonitoringCheckOutput) Probes() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.IntArrayOutput { return v.Probes }).(pulumi.IntArrayOutput)
}

// Check settings. Should contain exactly one nested block.
func (o SyntheticMonitoringCheckOutput) Settings() SyntheticMonitoringCheckSettingsOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) SyntheticMonitoringCheckSettingsOutput { return v.Settings }).(SyntheticMonitoringCheckSettingsOutput)
}

// Hostname to ping.
func (o SyntheticMonitoringCheckOutput) Target() pulumi.StringOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.StringOutput { return v.Target }).(pulumi.StringOutput)
}

// The tenant ID of the check.
func (o SyntheticMonitoringCheckOutput) TenantId() pulumi.IntOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.IntOutput { return v.TenantId }).(pulumi.IntOutput)
}

// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms),
// and the maximum 10 seconds (10000 ms).
func (o SyntheticMonitoringCheckOutput) Timeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SyntheticMonitoringCheck) pulumi.IntPtrOutput { return v.Timeout }).(pulumi.IntPtrOutput)
}

type SyntheticMonitoringCheckArrayOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringCheckArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SyntheticMonitoringCheck)(nil)).Elem()
}

func (o SyntheticMonitoringCheckArrayOutput) ToSyntheticMonitoringCheckArrayOutput() SyntheticMonitoringCheckArrayOutput {
	return o
}

func (o SyntheticMonitoringCheckArrayOutput) ToSyntheticMonitoringCheckArrayOutputWithContext(ctx context.Context) SyntheticMonitoringCheckArrayOutput {
	return o
}

func (o SyntheticMonitoringCheckArrayOutput) Index(i pulumi.IntInput) SyntheticMonitoringCheckOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SyntheticMonitoringCheck {
		return vs[0].([]*SyntheticMonitoringCheck)[vs[1].(int)]
	}).(SyntheticMonitoringCheckOutput)
}

type SyntheticMonitoringCheckMapOutput struct{ *pulumi.OutputState }

func (SyntheticMonitoringCheckMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SyntheticMonitoringCheck)(nil)).Elem()
}

func (o SyntheticMonitoringCheckMapOutput) ToSyntheticMonitoringCheckMapOutput() SyntheticMonitoringCheckMapOutput {
	return o
}

func (o SyntheticMonitoringCheckMapOutput) ToSyntheticMonitoringCheckMapOutputWithContext(ctx context.Context) SyntheticMonitoringCheckMapOutput {
	return o
}

func (o SyntheticMonitoringCheckMapOutput) MapIndex(k pulumi.StringInput) SyntheticMonitoringCheckOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SyntheticMonitoringCheck {
		return vs[0].(map[string]*SyntheticMonitoringCheck)[vs[1].(string)]
	}).(SyntheticMonitoringCheckOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringCheckInput)(nil)).Elem(), &SyntheticMonitoringCheck{})
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringCheckArrayInput)(nil)).Elem(), SyntheticMonitoringCheckArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SyntheticMonitoringCheckMapInput)(nil)).Elem(), SyntheticMonitoringCheckMap{})
	pulumi.RegisterOutputType(SyntheticMonitoringCheckOutput{})
	pulumi.RegisterOutputType(SyntheticMonitoringCheckArrayOutput{})
	pulumi.RegisterOutputType(SyntheticMonitoringCheckMapOutput{})
}
