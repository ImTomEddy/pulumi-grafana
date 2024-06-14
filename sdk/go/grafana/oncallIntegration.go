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

// Deprecated: grafana.index/oncallintegration.OncallIntegration has been deprecated in favor of grafana.oncall/integration.Integration
type OncallIntegration struct {
	pulumi.CustomResourceState

	// The Default route for all alerts from the given integration
	DefaultRoute OncallIntegrationDefaultRouteOutput `pulumi:"defaultRoute"`
	// The link for using in an integrated tool.
	Link pulumi.StringOutput `pulumi:"link"`
	// The name of the service integration.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
	// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrOutput `pulumi:"teamId"`
	// Jinja2 templates for Alert payload. An empty templates block will be ignored.
	Templates OncallIntegrationTemplatesPtrOutput `pulumi:"templates"`
	// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
	// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
	// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewOncallIntegration registers a new resource with the given unique name, arguments, and options.
func NewOncallIntegration(ctx *pulumi.Context,
	name string, args *OncallIntegrationArgs, opts ...pulumi.ResourceOption) (*OncallIntegration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DefaultRoute == nil {
		return nil, errors.New("invalid value for required argument 'DefaultRoute'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/oncallIntegration:OncallIntegration"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OncallIntegration
	err := ctx.RegisterResource("grafana:index/oncallIntegration:OncallIntegration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOncallIntegration gets an existing OncallIntegration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOncallIntegration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OncallIntegrationState, opts ...pulumi.ResourceOption) (*OncallIntegration, error) {
	var resource OncallIntegration
	err := ctx.ReadResource("grafana:index/oncallIntegration:OncallIntegration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OncallIntegration resources.
type oncallIntegrationState struct {
	// The Default route for all alerts from the given integration
	DefaultRoute *OncallIntegrationDefaultRoute `pulumi:"defaultRoute"`
	// The link for using in an integrated tool.
	Link *string `pulumi:"link"`
	// The name of the service integration.
	Name *string `pulumi:"name"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
	// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// Jinja2 templates for Alert payload. An empty templates block will be ignored.
	Templates *OncallIntegrationTemplates `pulumi:"templates"`
	// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
	// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
	// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
	Type *string `pulumi:"type"`
}

type OncallIntegrationState struct {
	// The Default route for all alerts from the given integration
	DefaultRoute OncallIntegrationDefaultRoutePtrInput
	// The link for using in an integrated tool.
	Link pulumi.StringPtrInput
	// The name of the service integration.
	Name pulumi.StringPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
	// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrInput
	// Jinja2 templates for Alert payload. An empty templates block will be ignored.
	Templates OncallIntegrationTemplatesPtrInput
	// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
	// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
	// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
	Type pulumi.StringPtrInput
}

func (OncallIntegrationState) ElementType() reflect.Type {
	return reflect.TypeOf((*oncallIntegrationState)(nil)).Elem()
}

type oncallIntegrationArgs struct {
	// The Default route for all alerts from the given integration
	DefaultRoute OncallIntegrationDefaultRoute `pulumi:"defaultRoute"`
	// The name of the service integration.
	Name *string `pulumi:"name"`
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
	// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId *string `pulumi:"teamId"`
	// Jinja2 templates for Alert payload. An empty templates block will be ignored.
	Templates *OncallIntegrationTemplates `pulumi:"templates"`
	// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
	// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
	// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a OncallIntegration resource.
type OncallIntegrationArgs struct {
	// The Default route for all alerts from the given integration
	DefaultRoute OncallIntegrationDefaultRouteInput
	// The name of the service integration.
	Name pulumi.StringPtrInput
	// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
	// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
	TeamId pulumi.StringPtrInput
	// Jinja2 templates for Alert payload. An empty templates block will be ignored.
	Templates OncallIntegrationTemplatesPtrInput
	// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
	// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
	// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
	Type pulumi.StringInput
}

func (OncallIntegrationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*oncallIntegrationArgs)(nil)).Elem()
}

type OncallIntegrationInput interface {
	pulumi.Input

	ToOncallIntegrationOutput() OncallIntegrationOutput
	ToOncallIntegrationOutputWithContext(ctx context.Context) OncallIntegrationOutput
}

func (*OncallIntegration) ElementType() reflect.Type {
	return reflect.TypeOf((**OncallIntegration)(nil)).Elem()
}

func (i *OncallIntegration) ToOncallIntegrationOutput() OncallIntegrationOutput {
	return i.ToOncallIntegrationOutputWithContext(context.Background())
}

func (i *OncallIntegration) ToOncallIntegrationOutputWithContext(ctx context.Context) OncallIntegrationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallIntegrationOutput)
}

// OncallIntegrationArrayInput is an input type that accepts OncallIntegrationArray and OncallIntegrationArrayOutput values.
// You can construct a concrete instance of `OncallIntegrationArrayInput` via:
//
//	OncallIntegrationArray{ OncallIntegrationArgs{...} }
type OncallIntegrationArrayInput interface {
	pulumi.Input

	ToOncallIntegrationArrayOutput() OncallIntegrationArrayOutput
	ToOncallIntegrationArrayOutputWithContext(context.Context) OncallIntegrationArrayOutput
}

type OncallIntegrationArray []OncallIntegrationInput

func (OncallIntegrationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OncallIntegration)(nil)).Elem()
}

func (i OncallIntegrationArray) ToOncallIntegrationArrayOutput() OncallIntegrationArrayOutput {
	return i.ToOncallIntegrationArrayOutputWithContext(context.Background())
}

func (i OncallIntegrationArray) ToOncallIntegrationArrayOutputWithContext(ctx context.Context) OncallIntegrationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallIntegrationArrayOutput)
}

// OncallIntegrationMapInput is an input type that accepts OncallIntegrationMap and OncallIntegrationMapOutput values.
// You can construct a concrete instance of `OncallIntegrationMapInput` via:
//
//	OncallIntegrationMap{ "key": OncallIntegrationArgs{...} }
type OncallIntegrationMapInput interface {
	pulumi.Input

	ToOncallIntegrationMapOutput() OncallIntegrationMapOutput
	ToOncallIntegrationMapOutputWithContext(context.Context) OncallIntegrationMapOutput
}

type OncallIntegrationMap map[string]OncallIntegrationInput

func (OncallIntegrationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OncallIntegration)(nil)).Elem()
}

func (i OncallIntegrationMap) ToOncallIntegrationMapOutput() OncallIntegrationMapOutput {
	return i.ToOncallIntegrationMapOutputWithContext(context.Background())
}

func (i OncallIntegrationMap) ToOncallIntegrationMapOutputWithContext(ctx context.Context) OncallIntegrationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OncallIntegrationMapOutput)
}

type OncallIntegrationOutput struct{ *pulumi.OutputState }

func (OncallIntegrationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OncallIntegration)(nil)).Elem()
}

func (o OncallIntegrationOutput) ToOncallIntegrationOutput() OncallIntegrationOutput {
	return o
}

func (o OncallIntegrationOutput) ToOncallIntegrationOutputWithContext(ctx context.Context) OncallIntegrationOutput {
	return o
}

// The Default route for all alerts from the given integration
func (o OncallIntegrationOutput) DefaultRoute() OncallIntegrationDefaultRouteOutput {
	return o.ApplyT(func(v *OncallIntegration) OncallIntegrationDefaultRouteOutput { return v.DefaultRoute }).(OncallIntegrationDefaultRouteOutput)
}

// The link for using in an integrated tool.
func (o OncallIntegrationOutput) Link() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallIntegration) pulumi.StringOutput { return v.Link }).(pulumi.StringOutput)
}

// The name of the service integration.
func (o OncallIntegrationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallIntegration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team
// with OnCall). You can then get the ID using the `onCall.getTeam` datasource.
func (o OncallIntegrationOutput) TeamId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OncallIntegration) pulumi.StringPtrOutput { return v.TeamId }).(pulumi.StringPtrOutput)
}

// Jinja2 templates for Alert payload. An empty templates block will be ignored.
func (o OncallIntegrationOutput) Templates() OncallIntegrationTemplatesPtrOutput {
	return o.ApplyT(func(v *OncallIntegration) OncallIntegrationTemplatesPtrOutput { return v.Templates }).(OncallIntegrationTemplatesPtrOutput)
}

// The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog,
// pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver,
// uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email, direct_paging, jira.
func (o OncallIntegrationOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *OncallIntegration) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type OncallIntegrationArrayOutput struct{ *pulumi.OutputState }

func (OncallIntegrationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OncallIntegration)(nil)).Elem()
}

func (o OncallIntegrationArrayOutput) ToOncallIntegrationArrayOutput() OncallIntegrationArrayOutput {
	return o
}

func (o OncallIntegrationArrayOutput) ToOncallIntegrationArrayOutputWithContext(ctx context.Context) OncallIntegrationArrayOutput {
	return o
}

func (o OncallIntegrationArrayOutput) Index(i pulumi.IntInput) OncallIntegrationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OncallIntegration {
		return vs[0].([]*OncallIntegration)[vs[1].(int)]
	}).(OncallIntegrationOutput)
}

type OncallIntegrationMapOutput struct{ *pulumi.OutputState }

func (OncallIntegrationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OncallIntegration)(nil)).Elem()
}

func (o OncallIntegrationMapOutput) ToOncallIntegrationMapOutput() OncallIntegrationMapOutput {
	return o
}

func (o OncallIntegrationMapOutput) ToOncallIntegrationMapOutputWithContext(ctx context.Context) OncallIntegrationMapOutput {
	return o
}

func (o OncallIntegrationMapOutput) MapIndex(k pulumi.StringInput) OncallIntegrationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OncallIntegration {
		return vs[0].(map[string]*OncallIntegration)[vs[1].(string)]
	}).(OncallIntegrationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OncallIntegrationInput)(nil)).Elem(), &OncallIntegration{})
	pulumi.RegisterInputType(reflect.TypeOf((*OncallIntegrationArrayInput)(nil)).Elem(), OncallIntegrationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OncallIntegrationMapInput)(nil)).Elem(), OncallIntegrationMap{})
	pulumi.RegisterOutputType(OncallIntegrationOutput{})
	pulumi.RegisterOutputType(OncallIntegrationArrayOutput{})
	pulumi.RegisterOutputType(OncallIntegrationMapOutput{})
}
