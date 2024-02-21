import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  data = [item for item in data if item['Continent'] == 'South America']

  countries = [x['Country'] for x in data]
  percentages = [x['World Population Percentage'] for x in data]
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)


# Permite ejecutar el archivo como script desde la terminal
if __name__ == '__main__':
  run()
