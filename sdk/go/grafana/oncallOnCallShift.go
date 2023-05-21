// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/on_call_shifts/)
//
// ## Import
//
// ```sh
//
//	$ pulumi import grafana:index/oncallOnCallShift:OncallOnCallShift on_call_shift_name {{on_call_shift_id}}
//
// ```
type OncallOnCallShift struct {
	pulumi.CustomResourceState

	// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	ByDays pulumi.StringArrayOutput `pulumi:"byDays"`
	// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
	ByMonthdays pulumi.IntArrayOutput `pulumi:"byMonthdays"`
	// This parameter takes a list of months. Valid values are 1 to 12
	ByMonths pulumi.IntArrayOutput `pulumi:"byMonths"`
	// The duration of the event.
	Duration pulumi.IntOutput `pulumi:"duration"`
	// The frequency of the event. Can be daily, weekly, monthly
	Frequency pulumi.StringPtrOutput `pulumi:"frequency"`
	// The positive integer representing at which intervals the recurrence rule repeats.
	Interval pulumi.IntPtrOutput `pulumi:"interval"`
	// The priority level. The higher the value, the higher the priority.
	Level pulumi.IntPtrOutput `pulumi:"level"`
	// The shift's name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The list of lists with on-call users (for rollingUsers event type)
	RollingUsers pulumi.StringArrayArrayOutput `pulumi:"rollingUsers"`
	// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
	Start pulumi.StringOutput `pulumi:"start"`
	// The index of the list of users in rolling_users, from which on-call rotation starts.
	StartRotationFromUserIndex pulumi.IntPtrOutput `pulumi:"startRotationFromUserIndex"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
	TeamId pulumi.StringPtrOutput `pulumi:"teamId"`
	// The shift's timezone.  Overrides schedule's timezone.
	TimeZone pulumi.StringPtrOutput `pulumi:"timeZone"`
	// The shift's type. Can be rolling*users, recurrent*event, single_event
	Type pulumi.StringOutput `pulumi:"type"`
	// The list of on-call users (for single*event and recurrent*event event type).
	Users pulumi.StringArrayOutput `pulumi:"users"`
	// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	WeekStart pulumi.StringPtrOutput `pulumi:"weekStart"`
}

// NewOncallOnCallShift registers a new resource with the given unique name, arguments, and options.
func NewOncallOnCallShift(ctx *pulumi.Context,
	name string, args *OncallOnCallShiftArgs, opts ...pulumi.ResourceOption) (*OncallOnCallShift, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Duration == nil {
		return nil, errors.New("invalid value for required argument 'Duration'")
	}
	if args.Start == nil {
		return nil, errors.New("invalid value for required argument 'Start'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource OncallOnCallShift
	err := ctx.RegisterResource("grafana:index/oncallOnCallShift:OncallOnCallShift", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOncallOnCallShift gets an existing OncallOnCallShift resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOncallOnCallShift(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OncallOnCallShiftState, opts ...pulumi.ResourceOption) (*OncallOnCallShift, error) {
	var resource OncallOnCallShift
	err := ctx.ReadResource("grafana:index/oncallOnCallShift:OncallOnCallShift", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OncallOnCallShift resources.
type oncallOnCallShiftState struct {
	// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	ByDays []string `pulumi:"byDays"`
	// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
	ByMonthdays []int `pulumi:"byMonthdays"`
	// This parameter takes a list of months. Valid values are 1 to 12
	ByMonths []int `pulumi:"byMonths"`
	// The duration of the event.
	Duration *int `pulumi:"duration"`
	// The frequency of the event. Can be daily, weekly, monthly
	Frequency *string `pulumi:"frequency"`
	// The positive integer representing at which intervals the recurrence rule repeats.
	Interval *int `pulumi:"interval"`
	// The priority level. The higher the value, the higher the priority.
	Level *int `pulumi:"level"`
	// The shift's name.
	Name *string `pulumi:"name"`
	// The list of lists with on-call users (for rollingUsers event type)
	RollingUsers [][]string `pulumi:"rollingUsers"`
	// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
	Start *string `pulumi:"start"`
	// The index of the list of users in rolling_users, from which on-call rotation starts.
	StartRotationFromUserIndex *int `pulumi:"startRotationFromUserIndex"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// The shift's timezone.  Overrides schedule's timezone.
	TimeZone *string `pulumi:"timeZone"`
	// The shift's type. Can be rolling*users, recurrent*event, single_event
	Type *string `pulumi:"type"`
	// The list of on-call users (for single*event and recurrent*event event type).
	Users []string `pulumi:"users"`
	// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	WeekStart *string `pulumi:"weekStart"`
}

type OncallOnCallShiftState struct {
	// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	ByDays pulumi.StringArrayInput
	// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
	ByMonthdays pulumi.IntArrayInput
	// This parameter takes a list of months. Valid values are 1 to 12
	ByMonths pulumi.IntArrayInput
	// The duration of the event.
	Duration pulumi.IntPtrInput
	// The frequency of the event. Can be daily, weekly, monthly
	Frequency pulumi.StringPtrInput
	// The positive integer representing at which intervals the recurrence rule repeats.
	Interval pulumi.IntPtrInput
	// The priority level. The higher the value, the higher the priority.
	Level pulumi.IntPtrInput
	// The shift's name.
	Name pulumi.StringPtrInput
	// The list of lists with on-call users (for rollingUsers event type)
	RollingUsers pulumi.StringArrayArrayInput
	// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
	Start pulumi.StringPtrInput
	// The index of the list of users in rolling_users, from which on-call rotation starts.
	StartRotationFromUserIndex pulumi.IntPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
	TeamId pulumi.StringPtrInput
	// The shift's timezone.  Overrides schedule's timezone.
	TimeZone pulumi.StringPtrInput
	// The shift's type. Can be rolling*users, recurrent*event, single_event
	Type pulumi.StringPtrInput
	// The list of on-call users (for single*event and recurrent*event event type).
	Users pulumi.StringArrayInput
	// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	WeekStart pulumi.StringPtrInput
}

func (OncallOnCallShiftState) ElementType() reflect.Type {
	return reflect.TypeOf((*oncallOnCallShiftState)(nil)).Elem()
}

type oncallOnCallShiftArgs struct {
	// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	ByDays []string `pulumi:"byDays"`
	// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
	ByMonthdays []int `pulumi:"byMonthdays"`
	// This parameter takes a list of months. Valid values are 1 to 12
	ByMonths []int `pulumi:"byMonths"`
	// The duration of the event.
	Duration int `pulumi:"duration"`
	// The frequency of the event. Can be daily, weekly, monthly
	Frequency *string `pulumi:"frequency"`
	// The positive integer representing at which intervals the recurrence rule repeats.
	Interval *int `pulumi:"interval"`
	// The priority level. The higher the value, the higher the priority.
	Level *int `pulumi:"level"`
	// The shift's name.
	Name *string `pulumi:"name"`
	// The list of lists with on-call users (for rollingUsers event type)
	RollingUsers [][]string `pulumi:"rollingUsers"`
	// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
	Start string `pulumi:"start"`
	// The index of the list of users in rolling_users, from which on-call rotation starts.
	StartRotationFromUserIndex *int `pulumi:"startRotationFromUserIndex"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// The shift's timezone.  Overrides schedule's timezone.
	TimeZone *string `pulumi:"timeZone"`
	// The shift's type. Can be rolling*users, recurrent*event, single_event
	Type string `pulumi:"type"`
	// The list of on-call users (for single*event and recurrent*event event type).
	Users []string `pulumi:"users"`
	// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	WeekStart *string `pulumi:"weekStart"`
}

// The set of arguments for constructing a OncallOnCallShift resource.
type OncallOnCallShiftArgs struct {
	// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	ByDays pulumi.StringArrayInput
	// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
	ByMonthdays pulumi.IntArrayInput
	// This parameter takes a list of months. Valid values are 1 to 12
	ByMonths pulumi.IntArrayInput
	// The duration of the event.
	Duration pulumi.IntInput
	// The frequency of the event. Can be daily, weekly, monthly
	Frequency pulumi.StringPtrInput
	// The positive integer representing at which intervals the recurrence rule repeats.
	Interval pulumi.IntPtrInput
	// The priority level. The higher the value, the higher the priority.
	Level pulumi.IntPtrInput
	// The shift's name.
	Name pulumi.StringPtrInput
	// The list of lists with on-call users (for rollingUsers event type)
	RollingUsers pulumi.StringArrayArrayInput
	// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
	Start pulumi.StringInput
	// The index of the list of users in rolling_users, from which on-call rotation starts.
	StartRotationFromUserIndex pulumi.IntPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
	TeamId pulumi.StringPtrInput
	// The shift's timezone.  Overrides schedule's timezone.
	TimeZone pulumi.StringPtrInput
	// The shift's type. Can be rolling*users, recurrent*event, single_event
	Type pulumi.StringInput
	// The list of on-call users (for single*event and recurrent*event event type).
	Users pulumi.StringArrayInput
	// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
	WeekStart pulumi.StringPtrInput
}

func (OncallOnCallShiftArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*oncallOnCallShiftArgs)(nil)).Elem()
}

type OncallOnCallShiftInput interface {
	pulumi.Input

	ToOncallOnCallShiftOutput() OncallOnCallShiftOutput
	ToOncallOnCallShiftOutputWithContext(ctx context.Context) OncallOnCallShiftOutput
}

func (*OncallOnCallShift) ElementType() reflect.Type {
	return reflect.TypeOf((**OncallOnCallShift)(nil)).Elem()
}

func (i *OncallOnCallShift) ToOncallOnCallShiftOutput() OncallOnCallShiftOutput {
	return i.ToOncallOnCallShiftOutputWithContext(context.Background())
}

func (i *OncallOnCallShift) ToOncallOnCallShiftOutputWithContext(ctx context.Context) OncallOnCallShiftOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallOnCallShiftOutput)
}

// OncallOnCallShiftArrayInput is an input type that accepts OncallOnCallShiftArray and OncallOnCallShiftArrayOutput values.
// You can construct a concrete instance of `OncallOnCallShiftArrayInput` via:
//
//	OncallOnCallShiftArray{ OncallOnCallShiftArgs{...} }
type OncallOnCallShiftArrayInput interface {
	pulumi.Input

	ToOncallOnCallShiftArrayOutput() OncallOnCallShiftArrayOutput
	ToOncallOnCallShiftArrayOutputWithContext(context.Context) OncallOnCallShiftArrayOutput
}

type OncallOnCallShiftArray []OncallOnCallShiftInput

func (OncallOnCallShiftArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OncallOnCallShift)(nil)).Elem()
}

func (i OncallOnCallShiftArray) ToOncallOnCallShiftArrayOutput() OncallOnCallShiftArrayOutput {
	return i.ToOncallOnCallShiftArrayOutputWithContext(context.Background())
}

func (i OncallOnCallShiftArray) ToOncallOnCallShiftArrayOutputWithContext(ctx context.Context) OncallOnCallShiftArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallOnCallShiftArrayOutput)
}

// OncallOnCallShiftMapInput is an input type that accepts OncallOnCallShiftMap and OncallOnCallShiftMapOutput values.
// You can construct a concrete instance of `OncallOnCallShiftMapInput` via:
//
//	OncallOnCallShiftMap{ "key": OncallOnCallShiftArgs{...} }
type OncallOnCallShiftMapInput interface {
	pulumi.Input

	ToOncallOnCallShiftMapOutput() OncallOnCallShiftMapOutput
	ToOncallOnCallShiftMapOutputWithContext(context.Context) OncallOnCallShiftMapOutput
}

type OncallOnCallShiftMap map[string]OncallOnCallShiftInput

func (OncallOnCallShiftMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OncallOnCallShift)(nil)).Elem()
}

func (i OncallOnCallShiftMap) ToOncallOnCallShiftMapOutput() OncallOnCallShiftMapOutput {
	return i.ToOncallOnCallShiftMapOutputWithContext(context.Background())
}

func (i OncallOnCallShiftMap) ToOncallOnCallShiftMapOutputWithContext(ctx context.Context) OncallOnCallShiftMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallOnCallShiftMapOutput)
}

type OncallOnCallShiftOutput struct{ *pulumi.OutputState }

func (OncallOnCallShiftOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OncallOnCallShift)(nil)).Elem()
}

func (o OncallOnCallShiftOutput) ToOncallOnCallShiftOutput() OncallOnCallShiftOutput {
	return o
}

func (o OncallOnCallShiftOutput) ToOncallOnCallShiftOutputWithContext(ctx context.Context) OncallOnCallShiftOutput {
	return o
}

// This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
func (o OncallOnCallShiftOutput) ByDays() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringArrayOutput { return v.ByDays }).(pulumi.StringArrayOutput)
}

// This parameter takes a list of days of the month.  Valid values are 1 to 31 or -31 to -1
func (o OncallOnCallShiftOutput) ByMonthdays() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntArrayOutput { return v.ByMonthdays }).(pulumi.IntArrayOutput)
}

// This parameter takes a list of months. Valid values are 1 to 12
func (o OncallOnCallShiftOutput) ByMonths() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntArrayOutput { return v.ByMonths }).(pulumi.IntArrayOutput)
}

// The duration of the event.
func (o OncallOnCallShiftOutput) Duration() pulumi.IntOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntOutput { return v.Duration }).(pulumi.IntOutput)
}

// The frequency of the event. Can be daily, weekly, monthly
func (o OncallOnCallShiftOutput) Frequency() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringPtrOutput { return v.Frequency }).(pulumi.StringPtrOutput)
}

// The positive integer representing at which intervals the recurrence rule repeats.
func (o OncallOnCallShiftOutput) Interval() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntPtrOutput { return v.Interval }).(pulumi.IntPtrOutput)
}

// The priority level. The higher the value, the higher the priority.
func (o OncallOnCallShiftOutput) Level() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntPtrOutput { return v.Level }).(pulumi.IntPtrOutput)
}

// The shift's name.
func (o OncallOnCallShiftOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The list of lists with on-call users (for rollingUsers event type)
func (o OncallOnCallShiftOutput) RollingUsers() pulumi.StringArrayArrayOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringArrayArrayOutput { return v.RollingUsers }).(pulumi.StringArrayArrayOutput)
}

// The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00")
func (o OncallOnCallShiftOutput) Start() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringOutput { return v.Start }).(pulumi.StringOutput)
}

// The index of the list of users in rolling_users, from which on-call rotation starts.
func (o OncallOnCallShiftOutput) StartRotationFromUserIndex() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.IntPtrOutput { return v.StartRotationFromUserIndex }).(pulumi.IntPtrOutput)
}

// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `getOncallTeam` datasource.
func (o OncallOnCallShiftOutput) TeamId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringPtrOutput { return v.TeamId }).(pulumi.StringPtrOutput)
}

// The shift's timezone.  Overrides schedule's timezone.
func (o OncallOnCallShiftOutput) TimeZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringPtrOutput { return v.TimeZone }).(pulumi.StringPtrOutput)
}

// The shift's type. Can be rolling*users, recurrent*event, single_event
func (o OncallOnCallShiftOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The list of on-call users (for single*event and recurrent*event event type).
func (o OncallOnCallShiftOutput) Users() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringArrayOutput { return v.Users }).(pulumi.StringArrayOutput)
}

// Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU
func (o OncallOnCallShiftOutput) WeekStart() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OncallOnCallShift) pulumi.StringPtrOutput { return v.WeekStart }).(pulumi.StringPtrOutput)
}

type OncallOnCallShiftArrayOutput struct{ *pulumi.OutputState }

func (OncallOnCallShiftArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OncallOnCallShift)(nil)).Elem()
}

func (o OncallOnCallShiftArrayOutput) ToOncallOnCallShiftArrayOutput() OncallOnCallShiftArrayOutput {
	return o
}

func (o OncallOnCallShiftArrayOutput) ToOncallOnCallShiftArrayOutputWithContext(ctx context.Context) OncallOnCallShiftArrayOutput {
	return o
}

func (o OncallOnCallShiftArrayOutput) Index(i pulumi.IntInput) OncallOnCallShiftOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OncallOnCallShift {
		return vs[0].([]*OncallOnCallShift)[vs[1].(int)]
	}).(OncallOnCallShiftOutput)
}

type OncallOnCallShiftMapOutput struct{ *pulumi.OutputState }

func (OncallOnCallShiftMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OncallOnCallShift)(nil)).Elem()
}

func (o OncallOnCallShiftMapOutput) ToOncallOnCallShiftMapOutput() OncallOnCallShiftMapOutput {
	return o
}

func (o OncallOnCallShiftMapOutput) ToOncallOnCallShiftMapOutputWithContext(ctx context.Context) OncallOnCallShiftMapOutput {
	return o
}

func (o OncallOnCallShiftMapOutput) MapIndex(k pulumi.StringInput) OncallOnCallShiftOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OncallOnCallShift {
		return vs[0].(map[string]*OncallOnCallShift)[vs[1].(string)]
	}).(OncallOnCallShiftOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OncallOnCallShiftInput)(nil)).Elem(), &OncallOnCallShift{})
	pulumi.RegisterInputType(reflect.TypeOf((*OncallOnCallShiftArrayInput)(nil)).Elem(), OncallOnCallShiftArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OncallOnCallShiftMapInput)(nil)).Elem(), OncallOnCallShiftMap{})
	pulumi.RegisterOutputType(OncallOnCallShiftOutput{})
	pulumi.RegisterOutputType(OncallOnCallShiftArrayOutput{})
	pulumi.RegisterOutputType(OncallOnCallShiftMapOutput{})
}
