// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package oncall

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/schedules/)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/onCall"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleSlackChannel, err := onCall.GetSlackChannel(ctx, &oncall.GetSlackChannelArgs{
//				Name: "example_slack_channel",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			exampleUserGroup, err := onCall.GetUserGroup(ctx, &oncall.GetUserGroupArgs{
//				SlackHandle: "example_slack_handle",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			// ICal based schedule
//			_, err = onCall.NewSchedule(ctx, "exampleScheduleSchedule", &onCall.ScheduleArgs{
//				Type:             pulumi.String("ical"),
//				IcalUrlPrimary:   pulumi.String("https://example.com/example_ical.ics"),
//				IcalUrlOverrides: pulumi.String("https://example.com/example_overrides_ical.ics"),
//				Slack: &oncall.ScheduleSlackArgs{
//					ChannelId:   pulumi.String(exampleSlackChannel.SlackId),
//					UserGroupId: pulumi.String(exampleUserGroup.SlackId),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			// Shift based schedule
//			_, err = onCall.NewSchedule(ctx, "exampleScheduleOnCall/scheduleSchedule", &onCall.ScheduleArgs{
//				Type:             pulumi.String("calendar"),
//				TimeZone:         pulumi.String("America/New_York"),
//				Shifts:           pulumi.StringArray{},
//				IcalUrlOverrides: pulumi.String("https://example.com/example_overrides_ical.ics"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// ```sh
// $ pulumi import grafana:onCall/schedule:Schedule name "{{ id }}"
// ```
type Schedule struct {
	pulumi.CustomResourceState

	// Enable overrides via web UI (it will ignore ical*url*overrides).
	EnableWebOverrides pulumi.BoolPtrOutput `pulumi:"enableWebOverrides"`
	// The URL of external iCal calendar which override primary events.
	IcalUrlOverrides pulumi.StringPtrOutput `pulumi:"icalUrlOverrides"`
	// The URL of the external calendar iCal file.
	IcalUrlPrimary pulumi.StringPtrOutput `pulumi:"icalUrlPrimary"`
	// The schedule's name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The list of ID's of on-call shifts.
	Shifts pulumi.StringArrayOutput `pulumi:"shifts"`
	// The Slack-specific settings for a schedule.
	Slack ScheduleSlackPtrOutput `pulumi:"slack"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrOutput `pulumi:"teamId"`
	// The schedule's time zone.
	TimeZone pulumi.StringPtrOutput `pulumi:"timeZone"`
	// The schedule's type. Valid values are `ical`, `calendar`.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewSchedule registers a new resource with the given unique name, arguments, and options.
func NewSchedule(ctx *pulumi.Context,
	name string, args *ScheduleArgs, opts ...pulumi.ResourceOption) (*Schedule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/oncallSchedule:OncallSchedule"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Schedule
	err := ctx.RegisterResource("grafana:onCall/schedule:Schedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSchedule gets an existing Schedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ScheduleState, opts ...pulumi.ResourceOption) (*Schedule, error) {
	var resource Schedule
	err := ctx.ReadResource("grafana:onCall/schedule:Schedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Schedule resources.
type scheduleState struct {
	// Enable overrides via web UI (it will ignore ical*url*overrides).
	EnableWebOverrides *bool `pulumi:"enableWebOverrides"`
	// The URL of external iCal calendar which override primary events.
	IcalUrlOverrides *string `pulumi:"icalUrlOverrides"`
	// The URL of the external calendar iCal file.
	IcalUrlPrimary *string `pulumi:"icalUrlPrimary"`
	// The schedule's name.
	Name *string `pulumi:"name"`
	// The list of ID's of on-call shifts.
	Shifts []string `pulumi:"shifts"`
	// The Slack-specific settings for a schedule.
	Slack *ScheduleSlack `pulumi:"slack"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// The schedule's time zone.
	TimeZone *string `pulumi:"timeZone"`
	// The schedule's type. Valid values are `ical`, `calendar`.
	Type *string `pulumi:"type"`
}

type ScheduleState struct {
	// Enable overrides via web UI (it will ignore ical*url*overrides).
	EnableWebOverrides pulumi.BoolPtrInput
	// The URL of external iCal calendar which override primary events.
	IcalUrlOverrides pulumi.StringPtrInput
	// The URL of the external calendar iCal file.
	IcalUrlPrimary pulumi.StringPtrInput
	// The schedule's name.
	Name pulumi.StringPtrInput
	// The list of ID's of on-call shifts.
	Shifts pulumi.StringArrayInput
	// The Slack-specific settings for a schedule.
	Slack ScheduleSlackPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrInput
	// The schedule's time zone.
	TimeZone pulumi.StringPtrInput
	// The schedule's type. Valid values are `ical`, `calendar`.
	Type pulumi.StringPtrInput
}

func (ScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*scheduleState)(nil)).Elem()
}

type scheduleArgs struct {
	// Enable overrides via web UI (it will ignore ical*url*overrides).
	EnableWebOverrides *bool `pulumi:"enableWebOverrides"`
	// The URL of external iCal calendar which override primary events.
	IcalUrlOverrides *string `pulumi:"icalUrlOverrides"`
	// The URL of the external calendar iCal file.
	IcalUrlPrimary *string `pulumi:"icalUrlPrimary"`
	// The schedule's name.
	Name *string `pulumi:"name"`
	// The list of ID's of on-call shifts.
	Shifts []string `pulumi:"shifts"`
	// The Slack-specific settings for a schedule.
	Slack *ScheduleSlack `pulumi:"slack"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// The schedule's time zone.
	TimeZone *string `pulumi:"timeZone"`
	// The schedule's type. Valid values are `ical`, `calendar`.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a Schedule resource.
type ScheduleArgs struct {
	// Enable overrides via web UI (it will ignore ical*url*overrides).
	EnableWebOverrides pulumi.BoolPtrInput
	// The URL of external iCal calendar which override primary events.
	IcalUrlOverrides pulumi.StringPtrInput
	// The URL of the external calendar iCal file.
	IcalUrlPrimary pulumi.StringPtrInput
	// The schedule's name.
	Name pulumi.StringPtrInput
	// The list of ID's of on-call shifts.
	Shifts pulumi.StringArrayInput
	// The Slack-specific settings for a schedule.
	Slack ScheduleSlackPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrInput
	// The schedule's time zone.
	TimeZone pulumi.StringPtrInput
	// The schedule's type. Valid values are `ical`, `calendar`.
	Type pulumi.StringInput
}

func (ScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*scheduleArgs)(nil)).Elem()
}

type ScheduleInput interface {
	pulumi.Input

	ToScheduleOutput() ScheduleOutput
	ToScheduleOutputWithContext(ctx context.Context) ScheduleOutput
}

func (*Schedule) ElementType() reflect.Type {
	return reflect.TypeOf((**Schedule)(nil)).Elem()
}

func (i *Schedule) ToScheduleOutput() ScheduleOutput {
	return i.ToScheduleOutputWithContext(context.Background())
}

func (i *Schedule) ToScheduleOutputWithContext(ctx context.Context) ScheduleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleOutput)
}

// ScheduleArrayInput is an input type that accepts ScheduleArray and ScheduleArrayOutput values.
// You can construct a concrete instance of `ScheduleArrayInput` via:
//
//	ScheduleArray{ ScheduleArgs{...} }
type ScheduleArrayInput interface {
	pulumi.Input

	ToScheduleArrayOutput() ScheduleArrayOutput
	ToScheduleArrayOutputWithContext(context.Context) ScheduleArrayOutput
}

type ScheduleArray []ScheduleInput

func (ScheduleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Schedule)(nil)).Elem()
}

func (i ScheduleArray) ToScheduleArrayOutput() ScheduleArrayOutput {
	return i.ToScheduleArrayOutputWithContext(context.Background())
}

func (i ScheduleArray) ToScheduleArrayOutputWithContext(ctx context.Context) ScheduleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleArrayOutput)
}

// ScheduleMapInput is an input type that accepts ScheduleMap and ScheduleMapOutput values.
// You can construct a concrete instance of `ScheduleMapInput` via:
//
//	ScheduleMap{ "key": ScheduleArgs{...} }
type ScheduleMapInput interface {
	pulumi.Input

	ToScheduleMapOutput() ScheduleMapOutput
	ToScheduleMapOutputWithContext(context.Context) ScheduleMapOutput
}

type ScheduleMap map[string]ScheduleInput

func (ScheduleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Schedule)(nil)).Elem()
}

func (i ScheduleMap) ToScheduleMapOutput() ScheduleMapOutput {
	return i.ToScheduleMapOutputWithContext(context.Background())
}

func (i ScheduleMap) ToScheduleMapOutputWithContext(ctx context.Context) ScheduleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleMapOutput)
}

type ScheduleOutput struct{ *pulumi.OutputState }

func (ScheduleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Schedule)(nil)).Elem()
}

func (o ScheduleOutput) ToScheduleOutput() ScheduleOutput {
	return o
}

func (o ScheduleOutput) ToScheduleOutputWithContext(ctx context.Context) ScheduleOutput {
	return o
}

// Enable overrides via web UI (it will ignore ical*url*overrides).
func (o ScheduleOutput) EnableWebOverrides() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Schedule) pulumi.BoolPtrOutput { return v.EnableWebOverrides }).(pulumi.BoolPtrOutput)
}

// The URL of external iCal calendar which override primary events.
func (o ScheduleOutput) IcalUrlOverrides() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringPtrOutput { return v.IcalUrlOverrides }).(pulumi.StringPtrOutput)
}

// The URL of the external calendar iCal file.
func (o ScheduleOutput) IcalUrlPrimary() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringPtrOutput { return v.IcalUrlPrimary }).(pulumi.StringPtrOutput)
}

// The schedule's name.
func (o ScheduleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The list of ID's of on-call shifts.
func (o ScheduleOutput) Shifts() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringArrayOutput { return v.Shifts }).(pulumi.StringArrayOutput)
}

// The Slack-specific settings for a schedule.
func (o ScheduleOutput) Slack() ScheduleSlackPtrOutput {
	return o.ApplyT(func(v *Schedule) ScheduleSlackPtrOutput { return v.Slack }).(ScheduleSlackPtrOutput)
}

// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
func (o ScheduleOutput) TeamId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringPtrOutput { return v.TeamId }).(pulumi.StringPtrOutput)
}

// The schedule's time zone.
func (o ScheduleOutput) TimeZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringPtrOutput { return v.TimeZone }).(pulumi.StringPtrOutput)
}

// The schedule's type. Valid values are `ical`, `calendar`.
func (o ScheduleOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Schedule) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type ScheduleArrayOutput struct{ *pulumi.OutputState }

func (ScheduleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Schedule)(nil)).Elem()
}

func (o ScheduleArrayOutput) ToScheduleArrayOutput() ScheduleArrayOutput {
	return o
}

func (o ScheduleArrayOutput) ToScheduleArrayOutputWithContext(ctx context.Context) ScheduleArrayOutput {
	return o
}

func (o ScheduleArrayOutput) Index(i pulumi.IntInput) ScheduleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Schedule {
		return vs[0].([]*Schedule)[vs[1].(int)]
	}).(ScheduleOutput)
}

type ScheduleMapOutput struct{ *pulumi.OutputState }

func (ScheduleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Schedule)(nil)).Elem()
}

func (o ScheduleMapOutput) ToScheduleMapOutput() ScheduleMapOutput {
	return o
}

func (o ScheduleMapOutput) ToScheduleMapOutputWithContext(ctx context.Context) ScheduleMapOutput {
	return o
}

func (o ScheduleMapOutput) MapIndex(k pulumi.StringInput) ScheduleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Schedule {
		return vs[0].(map[string]*Schedule)[vs[1].(string)]
	}).(ScheduleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleInput)(nil)).Elem(), &Schedule{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleArrayInput)(nil)).Elem(), ScheduleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleMapInput)(nil)).Elem(), ScheduleMap{})
	pulumi.RegisterOutputType(ScheduleOutput{})
	pulumi.RegisterOutputType(ScheduleArrayOutput{})
	pulumi.RegisterOutputType(ScheduleMapOutput{})
}
