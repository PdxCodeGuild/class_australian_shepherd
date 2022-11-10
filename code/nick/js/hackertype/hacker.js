let sampleCode = `struct ConvolutionNdCaptureState : public AutoGradCaptureState {
    bool input_requires_grad = false;
    bool weight_requires_grad = false;
    bool has_bias = false;
    bool bias_requires_grad = false;
    size_t input_index;
    size_t weight_index;

    @@ -58,10 +60,17 @@ Maybe<void> ConvolutionNd::Init(const OpExpr& op) {

  Maybe<void> ConvolutionNd::Capture(ConvolutionNdCaptureState* ctx, const TensorTuple& inputs,
                                    const TensorTuple& outputs, const AttrMap& attrs) const {
    CHECK_OR_RETURN(inputs.size() == 2 || inputs.size() == 3);  // NOLINT(maybe-need-error-msg)
    ctx->input_requires_grad = inputs.at(0)->requires_grad();
    ctx->weight_requires_grad = inputs.at(1)->requires_grad();
    if (inputs.size() == 3) {
      ctx->has_bias = true;
      ctx->bias_requires_grad = inputs.at(2)->requires_grad();
    }

    if (!ctx->input_requires_grad && !ctx->weight_requires_grad && !ctx->bias_requires_grad) {
      return Maybe<void>::Ok();
    }
    if (ctx->input_requires_grad) {
      ctx->weight_index = ctx->SaveTensorForBackward(inputs.at(1));  // weight
    }
    @@ -79,7 +88,11 @@ Maybe<void> ConvolutionNd::Capture(ConvolutionNdCaptureState* ctx, const TensorT

  Maybe<void> ConvolutionNd::Apply(const ConvolutionNdCaptureState* ctx, const TensorTuple& out_grads,
                                  TensorTuple* in_grads) const {
    if (ctx->has_bias) {
      in_grads->resize(3);
    } else {
      in_grads->resize(2);
    }
    size_t num_spatial_dims = ctx->kernel_size.size();
    if (ctx->input_requires_grad) {
      const auto& weight = ctx->SavedTensors().at(ctx->weight_index);
    @@ -94,6 +107,18 @@ Maybe<void> ConvolutionNd::Apply(const ConvolutionNdCaptureState* ctx, const Ten
          out_grads.at(0), input, num_spatial_dims, ctx->kernel_size, ctx->strides,
          ctx->padding_before, ctx->dilation_rate, ctx->groups, ctx->data_format));
    }
    if (ctx->bias_requires_grad) {
      std::vector<int32_t> dim;
      for (int i = 0; i < out_grads.at(0)->shape()->NumAxes(); ++i) {
        if ((ctx->data_format == "channels_first" && i == 1)
            || (ctx->data_format == "channels_last"
                && i == out_grads.at(0)->shape()->NumAxes() - 1)) {
          continue;
        }
        dim.push_back(i);
      }
      in_grads->at(2) = JUST(functional::ReduceSum(out_grads.at(0), dim, false));
    }
    return Maybe<void>::Ok();
  } 
  `

let codeArray = []
let codeLines = sampleCode.split("\n");
// console.log(codeLines);
codeLines.forEach(element => {
  let codeSnip = element.split("")
  codeArray.push(codeSnip)
  // console.log(codeSnip)
  // console.log(codeArray)
});

const para = document.getElementById("theCode");
let i = 0
document.addEventListener('keydown', (event) => {
  if (i < codeArray[0].length) {
    para.innerText += codeArray[0][i];
    i++
  }
  else {
    para.innerText += "\r\n";
    codeArray.shift()
    i = 0
  }
}
)

// Took this from hacker example site
function toggleCursor(){
  cursor.style.color="transparent"===cursor.style.color?"inherit":"transparent"
};
setInterval(toggleCursor,500);