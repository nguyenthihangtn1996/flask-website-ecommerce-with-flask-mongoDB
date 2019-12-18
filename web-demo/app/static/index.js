$( "#form_product" ).validate({
    rules: {
      name: {
        required: true,
        minlength:5,
        maxlength:50
      },
      username: {
        required: true,
        minlength:5,
        maxlength:30
      },
      password: {
        required: true,
        minlength: 5,
        maxlength:30
      }
    }
  });

