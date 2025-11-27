from mlx_lm import load, generate
import path_file


def call_model(prompt : str, number_of_answers : int = 1, show_probabilities : bool = False, arend_adapters : bool = True):
    if number_of_answers == 1 and arend_adapters:
        model, tokenizer = load(
            "mlx-community/Qwen2.5-Coder-1.5B-Instruct-Q6",
            adapter_path=path_file.adapter_path
        )
        return generate(model, tokenizer, prompt=prompt)

    if number_of_answers == 1 and not arend_adapters:
        model, tokenizer = load("mlx-community/Qwen2.5-Coder-1.5B-Instruct-Q6")
        return generate(model, tokenizer, prompt=prompt)
    # Doesn't work for now, as there is no implemented beam_search in mlx_lm TODO: make it work
    return False
    outputs = generate(model,
                       tokenizer,
                       prompt=prompt,
                       max_tokens=100,
                       num_beams=number_of_answers,  # number of sequences to consider
                       num_return_sequences=number_of_answers  # number of sequences to return
    )
    return outputs

# print(inference(prompt=r"\func f(x : Nat) : Nat", number_of_answers=1))