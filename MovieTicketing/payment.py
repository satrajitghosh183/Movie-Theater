import stripe

# Set up your Stripe API keys
stripe.api_key = 'your-stripe-api-key'


def process_payment(amount, currency, token):
  try:
    # Create a payment intent
    payment_intent = stripe.PaymentIntent.create(amount=amount,
                                                 currency=currency,
                                                 payment_method_types=['card'],
                                                 payment_method=token,
                                                 confirm=True)

    # Return the payment intent ID
    return payment_intent.id

  except stripe.error.CardError as e:
    # Handle card errors
    error_message = e.error.message
    print(f"Card Error: {error_message}")
    return None

  except stripe.error.StripeError as e:
    # Handle other Stripe errors
    error_message = e.error.message
    print(f"Stripe Error: {error_message}")
    return None

  except Exception as e:
    # Handle other exceptions
    print(f"Error: {str(e)}")
    return None
