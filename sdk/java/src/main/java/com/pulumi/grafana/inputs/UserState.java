// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class UserState extends com.pulumi.resources.ResourceArgs {

    public static final UserState Empty = new UserState();

    /**
     * The email address of the Grafana user.
     * 
     */
    @Import(name="email")
    private @Nullable Output<String> email;

    /**
     * @return The email address of the Grafana user.
     * 
     */
    public Optional<Output<String>> email() {
        return Optional.ofNullable(this.email);
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
    @Import(name="password")
    private @Nullable Output<String> password;

    /**
     * @return The password for the Grafana user.
     * 
     */
    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    /**
     * The numerical ID of the Grafana user.
     * 
     */
    @Import(name="userId")
    private @Nullable Output<Integer> userId;

    /**
     * @return The numerical ID of the Grafana user.
     * 
     */
    public Optional<Output<Integer>> userId() {
        return Optional.ofNullable(this.userId);
    }

    private UserState() {}

    private UserState(UserState $) {
        this.email = $.email;
        this.isAdmin = $.isAdmin;
        this.login = $.login;
        this.name = $.name;
        this.password = $.password;
        this.userId = $.userId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(UserState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private UserState $;

        public Builder() {
            $ = new UserState();
        }

        public Builder(UserState defaults) {
            $ = new UserState(Objects.requireNonNull(defaults));
        }

        /**
         * @param email The email address of the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder email(@Nullable Output<String> email) {
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
        public Builder password(@Nullable Output<String> password) {
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

        /**
         * @param userId The numerical ID of the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder userId(@Nullable Output<Integer> userId) {
            $.userId = userId;
            return this;
        }

        /**
         * @param userId The numerical ID of the Grafana user.
         * 
         * @return builder
         * 
         */
        public Builder userId(Integer userId) {
            return userId(Output.of(userId));
        }

        public UserState build() {
            return $;
        }
    }

}