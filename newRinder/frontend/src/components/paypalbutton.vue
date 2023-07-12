<template>
  <div>
    <div id="paypal-button-container"></div>
  </div>
  <div class="mx-auto w-50" ref="paypal"></div>
</template>

<script>
export default {
  name: "PayPalButton",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
        password2: "",
        plan: "",
      },
    };
  },
  mounted() {
    const script = document.createElement("script");
    script.src =
      "https://www.paypal.com/sdk/js?client-id=AW7Zjf5Dv2oj15br_xCYxlshsbkt5xI26Hj-KF6EWdQfi7H1M7Vi_pA_srclIaDWSd1pwKVgVVcABwx_";
    script.addEventListener("load", this.setLoaded);
    document.body.appendChild(script);
  },
  methods: {
    setLoaded: function () {
      window.paypal
        .Buttons({
          createOrder: function (data, actions) {
            return actions.order.create({
              purchase_units: [
                {
                  amount: {
                    value: "0.01",
                  },
                },
              ],
            });
          },
          onApprove: function (data, actions) {
            return actions.order.capture().then(function (details) {
              alert(
                "Transaction completed by " + details.payer.name.given_name
              );
            });
          },
        })
        .render(this.$refs.paypal);
    },
  },
};
</script>
