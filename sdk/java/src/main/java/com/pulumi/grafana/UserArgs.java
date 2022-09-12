// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class UserArgs extends com.pulumi.resources.ResourceArgs {

    public static final UserArgs Empty = new UserArgs();

    /**
     * The email address of the Grafana user.
     * 
     */
    @Import(name="email", required=true)
    private Output<String> email;

    /**
     * @return The email address of the Grafana user.
     * 
     */
    public Output<String> email() {
        return this.email;
    }

    /**
     * Whether to make user an admin. Defaults to `false`.
     * 
     */
    @Import(name="isAdmin")
    private @Nullable Output<Boolean> isAdmin;

    /**
     * @return Whether to make user an admin. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> isAdmin() {
        return Optional.ofNullable(this.isAdmin);
    }

    /**
     * The username for the Grafana user.
     * 
     */
    @Import(name="login")
    private @Nullable Output<String> login;

    /**
     * @return The username for the Grafana user.
     * 
     */
    public Optional<Output<String>> login() {
        return Optional.ofNullable(this.login);
    }

    /**
     * The display name for the Grafana user.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The display name for the Grafana user.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The password for the Grafana user.
     * 
     */
    @Import(name="password", required=true)
    private Output<String> password;

    /**
     * @return The password for the Grafana user.
     * 
     */
    public Output<String> password() {
        return this.password;
    }

    private UserArgs() {}

    private UserArgs(UserArgs $) {
        this.email = $.email;
        this.isAdmin = $.isAdmin;
        this.login = $.login;
        this.name = $.name;
        this.password = $.password;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(UserArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private UserArgs $;

        public Builder() {
            $ = new UserArgs();
        }

        public Builder(UserArgs defaults) {
            $ = new UserArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param email The email address of the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder email(Output<String> email) {
            $.email = email;
            return this;
        }

        /**
         * @param email The email address of the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder email(String email) {
            return email(Output.of(email));
        }

        /**
         * @param isAdmin Whether to make user an admin. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder isAdmin(@Nullable Output<Boolean> isAdmin) {
            $.isAdmin = isAdmin;
            return this;
        }

        /**
         * @param isAdmin Whether to make user an admin. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder isAdmin(Boolean isAdmin) {
            return isAdmin(Output.of(isAdmin));
        }

        /**
         * @param login The username for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder login(@Nullable Output<String> login) {
            $.login = login;
            return this;
        }

        /**
         * @param login The username for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder login(String login) {
            return login(Output.of(login));
        }

        /**
         * @param name The display name for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The display name for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param password The password for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder password(Output<String> password) {
            $.password = password;
            return this;
        }

        /**
         * @param password The password for the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder password(String password) {
            return password(Output.of(password));
        }

        public UserArgs build() {
            $.email = Objects.requireNonNull($.email, "expected parameter 'email' to be non-null");
            $.password = Objects.requireNonNull($.password, "expected parameter 'password' to be non-null");
            return $;
        }
    }

}