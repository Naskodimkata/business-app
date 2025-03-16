print('=== Welcome in Startuppers Hub! === ')

while True:
    print('\n1. Create a startup')
    print('2.Information about investors')
    print('3.Exit')

    choice = input('Pick an option(1-3):')

    if choice == '1':
        print('\n=== Create a startup ===')
        name = input('Name of startup')
        idea = input('Describe your idea:')
        problem = input('What problem is it going to solve')

        categories = {
            '1': 'Clothes',
            '2': 'Electric Vehicles',
            '3': 'Food supplement',
            '4': 'Programming'
        }

        recommendations = {
            'Clothes': 'Focus on quality materials, fashion trends and advertisement',
            'Electric Vehicles': 'Invest in batteries with great longevity and effective software',
            'Programming': 'Emphasize on pushing features in software',
            'Food supplement': 'Pay attention to the quality of the ingredients'

        }

        print('\nChoose a category')

        for key in categories:
            print(f'{key}. {categories[key]}')

        category_choice = input('Your choice:')

        if category_choice in categories:
            category = categories[category_choice]
            reccommendation = recommendations[category]
        else:
            category = 'Unknown'
            reccommendation = 'No reccommendation'

        budget = input('Prompt your planned budget in BGN')
        expenses = input('Prompt your expenses')

        print('\n=== Information about your startup ===')
        print(f'Name: {name}')
        print(f'Idea: {idea}')
        print(f'Problem: {problem}')
        print(f'Category: {category}')
        print(f'Reccomendation: {reccommendation}')
        print(f'Budget: {budget}')
        print(f'Expenses: {expenses}')
    elif choice == '2':
        print('\n=== Information about investors')
        print('As an investor you should pay attention to the following variables')
        print('Financial stability')
        print('Market potential')
        print('Business model and monetization')

        top_companies = {
            'Clothes': 'Nike, Adidas, Hugo',
            'Electric Vehicles': 'Tesla, Toyota, BWM',
            'Programming': 'Google, Amazon, Microsoft',
            'Food supplement': 'McDonald, KFC, Burgerking',

        }

        print('\nChoose a category to see the top companies')

        for key in top_companies:
            print(f'- {key}')

        category_choice = input('Your choice:')

        if category_choice in top_companies:
            print(f'The top companies in {category_choice}: {top_companies[category_choice]}')
        else:
            print('No information about this category')

    elif choice == '3'
        print('Thank you for using Startuppers Hub!')
        break
    else:
        print('invalid choice. Please try again!')
