from openai import OpenAI

TOKEN = ''
client = OpenAI(api_key = TOKEN)

def get_car_ai_bio(brand, model, year):
  prompt = '''
      Descrição de venda para o carro {} {} {} em 100 caracteres
  '''
  prompt = prompt.format(brand, model, year)
  response = client.completions.create(
    model='gpt-3.5-turbo',
    prompt=prompt,
    max_tokens=50
  )
  return response['choices'][0]['text']