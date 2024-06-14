// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring
{
    /// <summary>
    /// Synthetic Monitoring checks are tests that run on selected probes at defined
    /// intervals and report metrics and logs back to your Grafana Cloud account. The
    /// target for checks can be a domain name, a server, or a website, depending on
    /// what information you would like to gather about your endpoint. You can define
    /// multiple checks for a single endpoint to check different capabilities.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/create-checks/checks/)
    /// 
    /// ## Example Usage
    /// 
    /// ### DNS Basic
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var dns = new Grafana.SyntheticMonitoring.Check("dns", new()
    ///     {
    ///         Job = "DNS Defaults",
    ///         Target = "grafana.com",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Atlanta),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Dns = null,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### DNS Complex
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var dns = new Grafana.SyntheticMonitoring.Check("dns", new()
    ///     {
    ///         Job = "DNS Updated",
    ///         Target = "grafana.net",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Frankfurt),
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.London),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "baz" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Dns = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsDnsArgs
    ///             {
    ///                 IpVersion = "Any",
    ///                 Server = "8.8.4.4",
    ///                 Port = 8600,
    ///                 RecordType = "CNAME",
    ///                 Protocol = "TCP",
    ///                 ValidRCodes = new[]
    ///                 {
    ///                     "NOERROR",
    ///                     "NOTAUTH",
    ///                 },
    ///                 ValidateAnswerRrs = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsDnsValidateAnswerRrsArgs
    ///                 {
    ///                     FailIfMatchesRegexps = new[]
    ///                     {
    ///                         ".+-bad-stuff*",
    ///                     },
    ///                     FailIfNotMatchesRegexps = new[]
    ///                     {
    ///                         ".+-good-stuff*",
    ///                     },
    ///                 },
    ///                 ValidateAuthorityRrs = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsDnsValidateAuthorityRrsArgs
    ///                 {
    ///                     FailIfMatchesRegexps = new[]
    ///                     {
    ///                         ".+-bad-stuff*",
    ///                     },
    ///                     FailIfNotMatchesRegexps = new[]
    ///                     {
    ///                         ".+-good-stuff*",
    ///                     },
    ///                 },
    ///                 ValidateAdditionalRrs = new[]
    ///                 {
    ///                     new Grafana.SyntheticMonitoring.Inputs.CheckSettingsDnsValidateAdditionalRrArgs
    ///                     {
    ///                         FailIfMatchesRegexps = new[]
    ///                         {
    ///                             ".+-bad-stuff*",
    ///                         },
    ///                         FailIfNotMatchesRegexps = new[]
    ///                         {
    ///                             ".+-good-stuff*",
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### HTTP Basic
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var http = new Grafana.SyntheticMonitoring.Check("http", new()
    ///     {
    ///         Job = "HTTP Defaults",
    ///         Target = "https://grafana.com",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Atlanta),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Http = null,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### HTTP Complex
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var http = new Grafana.SyntheticMonitoring.Check("http", new()
    ///     {
    ///         Job = "HTTP Defaults",
    ///         Target = "https://grafana.org",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Bangalore),
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Mumbai),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Http = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsHttpArgs
    ///             {
    ///                 IpVersion = "V6",
    ///                 Method = "TRACE",
    ///                 Body = "and spirit",
    ///                 NoFollowRedirects = true,
    ///                 BearerToken = "asdfjkl;",
    ///                 ProxyUrl = "https://almost-there",
    ///                 FailIfSsl = true,
    ///                 FailIfNotSsl = true,
    ///                 CacheBustingQueryParamName = "pineapple",
    ///                 TlsConfig = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsHttpTlsConfigArgs
    ///                 {
    ///                     ServerName = "grafana.org",
    ///                     ClientCert = @"-----BEGIN CERTIFICATE-----
    /// MIIEljCCAn4CCQCKJPUQQxeO0zANBgkqhkiG9w0BAQsFADANMQswCQYDVQQGEwJT
    /// RTAeFw0yMTA1MjkxOTIyNTdaFw0yNDAzMTgxOTIyNTdaMA0xCzAJBgNVBAYTAlNF
    /// MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAnmbazDNUT0rSI4BpGZK+
    /// 0AJ+9FDkIYWJUtRLJoxw8CF+AobMFploYA2L2Myt80cTA1w8FrewjC8qlqdnrPWr
    /// h1ely2zsUljgi1/niH0ndjFzliL7UkinXQiAsTtYOrOQmzyd/o5PNdu7dz0m7stD
    /// BN/Sz5TlXZnA1/eJbqV/kqMau6b1MaBx8SbRfUG9+cSmUobFJwuktDrPuwJhcEkl
    /// iDmhEqu1GuZzmKvzPacLTVia1vSlmCTCu89NiHI8iGiiLtqNrapup7f8j5m3a3SL
    /// a+vXhplFj2piNl7Nc0dfuVgtEliTI+qUL2/+4A7gzRWZpHy21/LxMMXmBhdJW9En
    /// FWkev97VZLgb5TR3+qpSWmXcodjPy4dibvwsOMpdd+Q4AYulwvlDw5idRPVgGvk7
    /// qq03+w9ppZ5Fugws9k2CD9F/75JX2mCbRpkuPe8XXZ7bqrMaQgQMLOrs68HuiiCk
    /// FTklglq4DMKxnf/Y/T/MgIa9Q1o28YSevh6A7FnfPGARj2H2T4rToi+bC1Vf7qNB
    /// Z18bDpz99tRUTbyiRUSBMWLCGhU6c4HAqUrfrkpperOKFBQ3i38a79838oFdXHBW
    /// 6rx1t5cC3XwtEoUyeBKAygez8G1LDXbN3607MxVhAjhHKtPkYvuBfysSNU6JrR0z
    /// UV1IURJANt2UMuKgSEkG/IMCAwEAATANBgkqhkiG9w0BAQsFAAOCAgEAcipMhp/w
    /// yzfPy61faVAw9SPaMNRlnW9FCDC3N9CGOjo2knjXpObPzyzsJiUURTjrA9eFMpRA
    /// e2Rgn2j+nvm2XdLAlC4Kh8jqv/wCL0X6BTQMdN5aOhXdSiXtpXOMvXYY/dQ4ebRZ
    /// XeRCVWQD79JbV6/uyx0nCV3FVcU7L1P4UjxroefVr0soLPMirgxHmOxLnkoVgdcB
    /// tqufP5kJx9CIeJXPx3QQsk1XfEtxtUvuw4ZaZkQnNUqvGl7V+AZpur5Eqfv3zBi8
    /// QxxL7qGkARNssNWH2Ju+tqpM/UZRnjlFrDR4SXUgT0coTduBalUY6qHkciHmRpiP
    /// tf3SgpDeiCSOV2iVFGdaR1mz3muWoAYWFstcWN3a3HjjVugIi23yLN8Gv8CNeoH4
    /// prulinFCLrFgAh8SLAF8mOAZanT06LH8jOIFYrdUxH+ZeRBR0rLoFjUF+JB7UKD9
    /// 5TA+B4EBzQ1tMbGFU1DX79MjAejq0IV0Nzq+GMfBvLHxEf4+Oz8nqhDXQcJ6TdtY
    /// l3Lyw5zBvOL80SBK+Mr0UP7d9U3VXgbGHCYVJU6Ot1TwiGwahtWALRALA3TWeGkq
    /// 7kyD1H+nm+9lfKhuyBRQnRGBVyze2lAp7oxwshJuhBwEXosXFxq1Cy6QhPN77r6N
    /// vuhxvtppolNnyOgGxwG4zquqq2V5/+vKjKY=
    /// -----END CERTIFICATE-----
    /// ",
    ///                 },
    ///                 Headers = new[]
    ///                 {
    ///                     "Content-Type: multipart/form-data; boundary=something",
    ///                 },
    ///                 BasicAuth = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsHttpBasicAuthArgs
    ///                 {
    ///                     Username = "open",
    ///                     Password = "sesame",
    ///                 },
    ///                 ValidStatusCodes = new[]
    ///                 {
    ///                     200,
    ///                     201,
    ///                 },
    ///                 ValidHttpVersions = new[]
    ///                 {
    ///                     "HTTP/1.0",
    ///                     "HTTP/1.1",
    ///                     "HTTP/2.0",
    ///                 },
    ///                 FailIfBodyMatchesRegexps = new[]
    ///                 {
    ///                     ".*bad stuff.*",
    ///                 },
    ///                 FailIfBodyNotMatchesRegexps = new[]
    ///                 {
    ///                     ".*good stuff.*",
    ///                 },
    ///                 FailIfHeaderMatchesRegexps = new[]
    ///                 {
    ///                     new Grafana.SyntheticMonitoring.Inputs.CheckSettingsHttpFailIfHeaderMatchesRegexpArgs
    ///                     {
    ///                         Header = "Content-Type",
    ///                         Regexp = "application/soap*",
    ///                         AllowMissing = true,
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Ping Basic
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var ping = new Grafana.SyntheticMonitoring.Check("ping", new()
    ///     {
    ///         Job = "Ping Defaults",
    ///         Target = "grafana.com",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Atlanta),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Ping = null,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Ping Complex
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var ping = new Grafana.SyntheticMonitoring.Check("ping", new()
    ///     {
    ///         Job = "Ping Updated",
    ///         Target = "grafana.net",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Frankfurt),
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.London),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "baz" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Ping = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsPingArgs
    ///             {
    ///                 IpVersion = "Any",
    ///                 PayloadSize = 20,
    ///                 DontFragment = true,
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### TCP Basic
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var tcp = new Grafana.SyntheticMonitoring.Check("tcp", new()
    ///     {
    ///         Job = "TCP Defaults",
    ///         Target = "grafana.com:80",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Atlanta),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Tcp = null,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### TCP Complex
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var tcp = new Grafana.SyntheticMonitoring.Check("tcp", new()
    ///     {
    ///         Job = "TCP Defaults",
    ///         Target = "grafana.com:443",
    ///         Enabled = false,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Frankfurt),
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.London),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "baz" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Tcp = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsTcpArgs
    ///             {
    ///                 IpVersion = "V6",
    ///                 Tls = true,
    ///                 QueryResponses = new[]
    ///                 {
    ///                     new Grafana.SyntheticMonitoring.Inputs.CheckSettingsTcpQueryResponseArgs
    ///                     {
    ///                         Send = "howdy",
    ///                         Expect = "hi",
    ///                     },
    ///                     new Grafana.SyntheticMonitoring.Inputs.CheckSettingsTcpQueryResponseArgs
    ///                     {
    ///                         Send = "like this",
    ///                         Expect = "like that",
    ///                         StartTls = true,
    ///                     },
    ///                 },
    ///                 TlsConfig = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsTcpTlsConfigArgs
    ///                 {
    ///                     ServerName = "grafana.com",
    ///                     CaCert = @"-----BEGIN CERTIFICATE-----
    /// MIIEljCCAn4CCQCKJPUQQxeO0zANBgkqhkiG9w0BAQsFADANMQswCQYDVQQGEwJT
    /// RTAeFw0yMTA1MjkxOTIyNTdaFw0yNDAzMTgxOTIyNTdaMA0xCzAJBgNVBAYTAlNF
    /// MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAnmbazDNUT0rSI4BpGZK+
    /// 0AJ+9FDkIYWJUtRLJoxw8CF+AobMFploYA2L2Myt80cTA1w8FrewjC8qlqdnrPWr
    /// h1ely2zsUljgi1/niH0ndjFzliL7UkinXQiAsTtYOrOQmzyd/o5PNdu7dz0m7stD
    /// BN/Sz5TlXZnA1/eJbqV/kqMau6b1MaBx8SbRfUG9+cSmUobFJwuktDrPuwJhcEkl
    /// iDmhEqu1GuZzmKvzPacLTVia1vSlmCTCu89NiHI8iGiiLtqNrapup7f8j5m3a3SL
    /// a+vXhplFj2piNl7Nc0dfuVgtEliTI+qUL2/+4A7gzRWZpHy21/LxMMXmBhdJW9En
    /// FWkev97VZLgb5TR3+qpSWmXcodjPy4dibvwsOMpdd+Q4AYulwvlDw5idRPVgGvk7
    /// qq03+w9ppZ5Fugws9k2CD9F/75JX2mCbRpkuPe8XXZ7bqrMaQgQMLOrs68HuiiCk
    /// FTklglq4DMKxnf/Y/T/MgIa9Q1o28YSevh6A7FnfPGARj2H2T4rToi+bC1Vf7qNB
    /// Z18bDpz99tRUTbyiRUSBMWLCGhU6c4HAqUrfrkpperOKFBQ3i38a79838oFdXHBW
    /// 6rx1t5cC3XwtEoUyeBKAygez8G1LDXbN3607MxVhAjhHKtPkYvuBfysSNU6JrR0z
    /// UV1IURJANt2UMuKgSEkG/IMCAwEAATANBgkqhkiG9w0BAQsFAAOCAgEAcipMhp/w
    /// yzfPy61faVAw9SPaMNRlnW9FCDC3N9CGOjo2knjXpObPzyzsJiUURTjrA9eFMpRA
    /// e2Rgn2j+nvm2XdLAlC4Kh8jqv/wCL0X6BTQMdN5aOhXdSiXtpXOMvXYY/dQ4ebRZ
    /// XeRCVWQD79JbV6/uyx0nCV3FVcU7L1P4UjxroefVr0soLPMirgxHmOxLnkoVgdcB
    /// tqufP5kJx9CIeJXPx3QQsk1XfEtxtUvuw4ZaZkQnNUqvGl7V+AZpur5Eqfv3zBi8
    /// QxxL7qGkARNssNWH2Ju+tqpM/UZRnjlFrDR4SXUgT0coTduBalUY6qHkciHmRpiP
    /// tf3SgpDeiCSOV2iVFGdaR1mz3muWoAYWFstcWN3a3HjjVugIi23yLN8Gv8CNeoH4
    /// prulinFCLrFgAh8SLAF8mOAZanT06LH8jOIFYrdUxH+ZeRBR0rLoFjUF+JB7UKD9
    /// 5TA+B4EBzQ1tMbGFU1DX79MjAejq0IV0Nzq+GMfBvLHxEf4+Oz8nqhDXQcJ6TdtY
    /// l3Lyw5zBvOL80SBK+Mr0UP7d9U3VXgbGHCYVJU6Ot1TwiGwahtWALRALA3TWeGkq
    /// 7kyD1H+nm+9lfKhuyBRQnRGBVyze2lAp7oxwshJuhBwEXosXFxq1Cy6QhPN77r6N
    /// vuhxvtppolNnyOgGxwG4zquqq2V5/+vKjKY=
    /// -----END CERTIFICATE-----
    /// ",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Traceroute Basic
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var traceroute = new Grafana.SyntheticMonitoring.Check("traceroute", new()
    ///     {
    ///         Job = "Traceroute defaults",
    ///         Target = "grafana.com",
    ///         Enabled = false,
    ///         Frequency = 120000,
    ///         Timeout = 30000,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Atlanta),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "bar" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Traceroute = null,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Traceroute Complex
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumi.Grafana;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = Grafana.SyntheticMonitoring.GetProbes.Invoke();
    /// 
    ///     var traceroute = new Grafana.SyntheticMonitoring.Check("traceroute", new()
    ///     {
    ///         Job = "Traceroute complex",
    ///         Target = "grafana.net",
    ///         Enabled = false,
    ///         Frequency = 120000,
    ///         Timeout = 30000,
    ///         Probes = new[]
    ///         {
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.Frankfurt),
    ///             main.Apply(getProbesResult =&gt; getProbesResult.Probes?.London),
    ///         },
    ///         Labels = 
    ///         {
    ///             { "foo", "baz" },
    ///         },
    ///         Settings = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsArgs
    ///         {
    ///             Traceroute = new Grafana.SyntheticMonitoring.Inputs.CheckSettingsTracerouteArgs
    ///             {
    ///                 MaxHops = 25,
    ///                 MaxUnknownHops = 10,
    ///                 PtrLookup = false,
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:syntheticMonitoring/check:Check name "{{ id }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:syntheticMonitoring/check:Check")]
    public partial class Check : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/). Defaults to `none`.
        /// </summary>
        [Output("alertSensitivity")]
        public Output<string?> AlertSensitivity { get; private set; } = null!;

        /// <summary>
        /// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
        /// </summary>
        [Output("basicMetricsOnly")]
        public Output<bool?> BasicMetricsOnly { get; private set; } = null!;

        /// <summary>
        /// Whether to enable the check. Defaults to `true`.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms). Defaults to `60000`.
        /// </summary>
        [Output("frequency")]
        public Output<int?> Frequency { get; private set; } = null!;

        /// <summary>
        /// Name used for job label.
        /// </summary>
        [Output("job")]
        public Output<string> Job { get; private set; } = null!;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// List of probe location IDs where this target will be checked from.
        /// </summary>
        [Output("probes")]
        public Output<ImmutableArray<int>> Probes { get; private set; } = null!;

        /// <summary>
        /// Check settings. Should contain exactly one nested block.
        /// </summary>
        [Output("settings")]
        public Output<Outputs.CheckSettings> Settings { get; private set; } = null!;

        /// <summary>
        /// Hostname to ping.
        /// </summary>
        [Output("target")]
        public Output<string> Target { get; private set; } = null!;

        /// <summary>
        /// The tenant ID of the check.
        /// </summary>
        [Output("tenantId")]
        public Output<int> TenantId { get; private set; } = null!;

        /// <summary>
        /// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
        /// </summary>
        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;


        /// <summary>
        /// Create a Check resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Check(string name, CheckArgs args, CustomResourceOptions? options = null)
            : base("grafana:syntheticMonitoring/check:Check", name, args ?? new CheckArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Check(string name, Input<string> id, CheckState? state = null, CustomResourceOptions? options = null)
            : base("grafana:syntheticMonitoring/check:Check", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "grafana:index/syntheticMonitoringCheck:SyntheticMonitoringCheck" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Check resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Check Get(string name, Input<string> id, CheckState? state = null, CustomResourceOptions? options = null)
        {
            return new Check(name, id, state, options);
        }
    }

    public sealed class CheckArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/). Defaults to `none`.
        /// </summary>
        [Input("alertSensitivity")]
        public Input<string>? AlertSensitivity { get; set; }

        /// <summary>
        /// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
        /// </summary>
        [Input("basicMetricsOnly")]
        public Input<bool>? BasicMetricsOnly { get; set; }

        /// <summary>
        /// Whether to enable the check. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms). Defaults to `60000`.
        /// </summary>
        [Input("frequency")]
        public Input<int>? Frequency { get; set; }

        /// <summary>
        /// Name used for job label.
        /// </summary>
        [Input("job", required: true)]
        public Input<string> Job { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("probes", required: true)]
        private InputList<int>? _probes;

        /// <summary>
        /// List of probe location IDs where this target will be checked from.
        /// </summary>
        public InputList<int> Probes
        {
            get => _probes ?? (_probes = new InputList<int>());
            set => _probes = value;
        }

        /// <summary>
        /// Check settings. Should contain exactly one nested block.
        /// </summary>
        [Input("settings", required: true)]
        public Input<Inputs.CheckSettingsArgs> Settings { get; set; } = null!;

        /// <summary>
        /// Hostname to ping.
        /// </summary>
        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        /// <summary>
        /// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        public CheckArgs()
        {
        }
        public static new CheckArgs Empty => new CheckArgs();
    }

    public sealed class CheckState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/configure-alerts/synthetic-monitoring-alerting/). Defaults to `none`.
        /// </summary>
        [Input("alertSensitivity")]
        public Input<string>? AlertSensitivity { get; set; }

        /// <summary>
        /// Metrics are reduced by default. Set this to `false` if you'd like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
        /// </summary>
        [Input("basicMetricsOnly")]
        public Input<bool>? BasicMetricsOnly { get; set; }

        /// <summary>
        /// Whether to enable the check. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable value is 1 second (1000 ms), and the maximum is 1 hour (3600000 ms). Defaults to `60000`.
        /// </summary>
        [Input("frequency")]
        public Input<int>? Frequency { get; set; }

        /// <summary>
        /// Name used for job label.
        /// </summary>
        [Input("job")]
        public Input<string>? Job { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("probes")]
        private InputList<int>? _probes;

        /// <summary>
        /// List of probe location IDs where this target will be checked from.
        /// </summary>
        public InputList<int> Probes
        {
            get => _probes ?? (_probes = new InputList<int>());
            set => _probes = value;
        }

        /// <summary>
        /// Check settings. Should contain exactly one nested block.
        /// </summary>
        [Input("settings")]
        public Input<Inputs.CheckSettingsGetArgs>? Settings { get; set; }

        /// <summary>
        /// Hostname to ping.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        /// <summary>
        /// The tenant ID of the check.
        /// </summary>
        [Input("tenantId")]
        public Input<int>? TenantId { get; set; }

        /// <summary>
        /// Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        public CheckState()
        {
        }
        public static new CheckState Empty => new CheckState();
    }
}
