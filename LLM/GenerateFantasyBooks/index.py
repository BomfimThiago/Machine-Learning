import openai

openai.api_key = ""

response = openai.File.create(
    file=open("assets/training_data.txt"),
    purpose="fine-tune"
)

file_id = response['id']

# start the fine-tuning process
fine_tuned_model = openai.FineTune.create(
    training_file=file_id,
    model="gpt-4.0-turbo",
    n_epochs=4,
)

print("Fine-tuned model ID:", fine_tuned_model['id'])


status = openai.FineTune.retrieve(fine_tuned_model['id'])
print("Fine-tuning status:", status['status'])


