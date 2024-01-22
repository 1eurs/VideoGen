import requests
import random
def create_story_prompt(topic):
    return f"""Imagine a scenario in the world of {topic}. The main character, deeply involved in their respective field, faces a critical moment or dilemma. They pose a thought-provoking, rhetorical question that reflects their challenge or situation.

For example:

In the world of K-pop: A trainee or performer questioning the nature of their path to stardom.
In the realm of MCTS algorithms: A programmer or AI entity contemplating the complexities of decision-making processes.
Within a Valorant game: A player or character musing about strategy, skill, and victory.
In the microscopic world of white blood cells: A cell or pathogen pondering the intricacies of the immune response.

Then, in an unexpected twist, an inanimate object, a virtual entity, or even the environment itself responds with wisdom or insight that is both profound and slightly exaggerated. This response should reveal a deeper understanding of the field and include a twist that reflects the unique aspects of the chosen topic.

The scenario should conclude with a realization or an ironic twist that encapsulates a deeper truth or an amusing insight into the chosen topic.
The scenario should be around 100 sentence long.
ouput should be only the scenario and nothing else.

"""
def create_story_prompt2(topic):
    return f"""
    Imagine a scenario in any this {topic} field/world - it could be science, technology, art, history, fantasy, or any other realm. In this scenario, the main character or entity, deeply involved in their field, is confronted with a thought-provoking situation or dilemma.

    They should ask a rhetorical question in the style of: 'Are you [X] because you [Y]? Or are you [Y] because you [X]?' This question should reflect a paradox, a deep truth, or an ironic twist related to their field or situation.

    Examples:
    - In the field of technology: 'Are you intelligent because you learn from data? Or do you learn from data because you are intelligent?'
    - In the realm of art: 'Is this art moving because it's expressive? Or is it expressive because it moves us?'
    - In a historical context: 'Did the empire fall because of its leaders? Or did the leaders fail because of the empire?'
    - In a fantasy world: 'Does the wizard cast spells because he's powerful? Or is he powerful because he casts spells?'

    The scenario should then unfold with an unexpected response or development that provides insight or commentary, reflecting the paradoxical nature of the question. This response can be from another character, the environment, or even an inanimate object.

    The conclusion should offer a realization, an ironic twist, or a humorous insight that encapsulates a deeper understanding or a unique perspective of the chosen topic.
    
    The scenario should be around 100 sentence long.
    The output should be only the story.
    """




def create_story_prompt3(topic):
    return f'''Once the new McDonald's employee was foolish enough to ask for a pay rise, the other employees exclaimed in shock. They knew that he was finished. The manager, disgusted by this outrageous request, simply laughed and began to open his domain. Domain expansion. Infinite Burgers.

as the integrator got out his pen and began solving the problem he asked the function are you zero because we're integrating along a closed contour or are we integrating along a closed contour because you're zero the function then replied stand proud you are strong but not might win for unbeknownst to the integrator the function was not analytic and has a singularity within the contour in that moment the function could have saved itself but it did not know two key things the first is always bet on the integrator and the second is that the integrator new residue theorem

As the carbon dioxide and water wander within the chloroplasts of plant cells, converting carbon dioxide and water into glucose and oxygen, the plant cell question the water. Are you oxidized because you're losing electrons? Or are you losing electrons because you're oxidized, to which the water replied? Stand proud, you're strong, but I'm the one who left it all behind. Before the chloroplast uses domain expansion, light absorption, and the cursive techniques, water splitting and carbon fixation, the plant cell asks the chlorophyll, can you split water? However, it did not know two key things. The first is that you always bet on the chlorophyll and the second is that throughout plant cells and the chloroplast, the chlorophyll alone is the absorbent one. The chlorophyll replied, if I couldn't find sunlight I might have a little trouble, but would you lose? Now, I'd win.

As the student opened his notebook domain and started solving the linear system, he asked to the system, Are you compatible because the ranks of the complete and incomplete matrices are the same? Or are the ranks of the matrices the same because you're compatible? The system simply answered, would you believe me? The student said, not, I'd find the determinants. In the next 4 minutes and 11 seconds, the student found that the solution of the system was only one, due to the Ruchek-Capelli theorem. In that moment, the system fully thought the student wouldn't find the solution, but he didn't know two things. The first is, always bet on the student. The other one is that with this treasure he summons, and his overwhelming utility, the student knew Kramer's rule.

As the student got out his pen and began solving them, square root of minus one, he asked the square root, Are you I? Because you are the square root of minus one, or are you the square root of minus one? Because you are I, the square root then replied, Stand proud, you are strong, but nah, I'd square up, for unbeknownst to the student, the square root was not telling him some and has something, it's hiding, in that moment, the square root could have saved itself, but didn't know to key things. The first is always better, the student, and the second, the student, new imaginary numbers.

As Einstein was about to discover the special theory of relativity and deeper understanding behind the laws of motion, Newton himself rose from the dead and asked, how many Tesla fingers am I in terms of strength? At that moment, Einstein opened his domain. Domain expansion, special relativity, E equals MC squared.

As the student got up from his desk in defiance, the teacher asked him, are you failing this class because you're disrespectful? Or are you disrespectful because you're failing this class? The boy unperturbed by this activated his technique, cursed speech. Instead, are you working a dead end job at a school? Because you are a loser who peaked at 15. Or are you a loser who peaked at 15 because you are now working a dead end job at a school? Unbeknownst to the boy, the teacher ears were reinforced with cursed energy, allowing the teacher to time necessary to open up their domain. Infinite belt lashing, the teacher then took off his belt and beat the boy senselessly.

 When the UK asked the big three Russia, America, and China if aliens invaded Earth,  do you think we would have a chance? The three countries looked back at each other  and then gave the UK a smug smirk. They all said if aliens invaded it would definitely  cause us trouble. But if the three of us all teamed up, it would tip the invasion in our  favor. The UK then said okay, but do you think we would lose? All three of these powerhouse  countries answered back, saying nah, we'd win.

As the student got up from his desk in defiance, the teacher asked him, are you failing this class because you're disrespectful? Or are you disrespectful because you're failing this class? The boy unperturbed by this activated his technique, cursed speech. Instead, are you working a dead end job at a school? Because you are a loser who peaked at 15. Or are you a loser who peaked at 15 because you are now working a dead end job at a school? Unbeknownst to the boy, the teacher ears were reinforced with cursed energy, allowing the teacher to time necessary to open up their domain. Infinite belt lashing, the teacher then took off his belt and beat the boy senselessly.


make same style story telling but about {topic}. No matter what is the topic ouput same style story and reserche the topic to make ur own story but same style .. make it around 100 words and only output the story '''

def create_story_prompt4(topic):
    return f'''Once the new McDonald's employee was foolish enough to ask for a pay rise, the other employees exclaimed in shock. They knew that he was finished. The manager, disgusted by this outrageous request, simply laughed and began to open his domain. Domain expansion. Infinite Burgers.

as the integrator got out his pen and began solving the problem he asked the function are you zero because we're integrating along a closed contour or are we integrating along a closed contour because you're zero the function then replied stand proud you are strong but not might win for unbeknownst to the integrator the function was not analytic and has a singularity within the contour in that moment the function could have saved itself but it did not know two key things the first is always bet on the integrator and the second is that the integrator new residue theorem

As the carbon dioxide and water wander within the chloroplasts of plant cells, converting carbon dioxide and water into glucose and oxygen, the plant cell question the water. Are you oxidized because you're losing electrons? Or are you losing electrons because you're oxidized, to which the water replied? Stand proud, you're strong, but I'm the one who left it all behind. Before the chloroplast uses domain expansion, light absorption, and the cursive techniques, water splitting and carbon fixation, the plant cell asks the chlorophyll, can you split water? However, it did not know two key things. The first is that you always bet on the chlorophyll and the second is that throughout plant cells and the chloroplast, the chlorophyll alone is the absorbent one. The chlorophyll replied, if I couldn't find sunlight I might have a little trouble, but would you lose? Now, I'd win.

As the student opened his notebook domain and started solving the linear system, he asked to the system, Are you compatible because the ranks of the complete and incomplete matrices are the same? Or are the ranks of the matrices the same because you're compatible? The system simply answered, would you believe me? The student said, not, I'd find the determinants. In the next 4 minutes and 11 seconds, the student found that the solution of the system was only one, due to the Ruchek-Capelli theorem. In that moment, the system fully thought the student wouldn't find the solution, but he didn't know two things. The first is, always bet on the student. The other one is that with this treasure he summons, and his overwhelming utility, the student knew Kramer's rule.

As the student got out his pen and began solving them, square root of minus one, he asked the square root, Are you I? Because you are the square root of minus one, or are you the square root of minus one? Because you are I, the square root then replied, Stand proud, you are strong, but nah, I'd square up, for unbeknownst to the student, the square root was not telling him some and has something, it's hiding, in that moment, the square root could have saved itself, but didn't know to key things. The first is always better, the student, and the second, the student, new imaginary numbers.

As Einstein was about to discover the special theory of relativity and deeper understanding behind the laws of motion, Newton himself rose from the dead and asked, how many Tesla fingers am I in terms of strength? At that moment, Einstein opened his domain. Domain expansion, special relativity, E equals MC squared.

As the student got up from his desk in defiance, the teacher asked him, are you failing this class because you're disrespectful? Or are you disrespectful because you're failing this class? The boy unperturbed by this activated his technique, cursed speech. Instead, are you working a dead end job at a school? Because you are a loser who peaked at 15. Or are you a loser who peaked at 15 because you are now working a dead end job at a school? Unbeknownst to the boy, the teacher ears were reinforced with cursed energy, allowing the teacher to time necessary to open up their domain. Infinite belt lashing, the teacher then took off his belt and beat the boy senselessly.

 When the UK asked the big three Russia, America, and China if aliens invaded Earth,  do you think we would have a chance? The three countries looked back at each other  and then gave the UK a smug smirk. They all said if aliens invaded it would definitely  cause us trouble. But if the three of us all teamed up, it would tip the invasion in our  favor. The UK then said okay, but do you think we would lose? All three of these powerhouse  countries answered back, saying nah, we'd win.

As the student got up from his desk in defiance, the teacher asked him, are you failing this class because you're disrespectful? Or are you disrespectful because you're failing this class? The boy unperturbed by this activated his technique, cursed speech. Instead, are you working a dead end job at a school? Because you are a loser who peaked at 15. Or are you a loser who peaked at 15 because you are now working a dead end job at a school? Unbeknownst to the boy, the teacher ears were reinforced with cursed energy, allowing the teacher to time necessary to open up their domain. Infinite belt lashing, the teacher then took off his belt and beat the boy senselessly.


Imagine a scenario where {topic} is the focal point. In a moment of curiosity, someone questions {topic} in a unique way.  {topic} responds with a twist, revealing a hidden truth. Unbeknownst to them, [character] holds a secret or knowledge that changes everything. Explore this situation in the same style as the previous stories, with a humorous or unexpected twist.

make same style story telling but about {topic}. No matter what is the topic ouput same style story and reserche the topic to make ur own story but same style .. make it around 100 words and only output the story '''



def create_story_prompt5(topic):
    return f'''"Generate a whimsical and humorous narrative centered around the theme of {topic}, with characters confidently using phrases like 'Nah, I'd [action]' or posing questions in the format of 'Are you [condition] because, or [condition] because you're [condition]?' Encourage the use of character responses in the style of '[Character] then replied [assertion],' and incorporate moments where characters are unaware of crucial information, leading to unexpected outcomes within the realm of {topic}. Explore the application of principles or advice, stating 'The first is [advice or principle], and the second is [another advice or principle],' specifically related to the challenges and quirks of {topic}, to add a layer of humor and perspective. Additionally, introduce critical moments where characters could have taken specific actions related to {topic}, but for a given reason, they didn't. Include sequences where characters employ certain techniques or concepts within the context of {topic}, resulting in surprising or unexpected outcomes. Story length around 100 words. Output should be only the story and nothing else."'''


def generate_response(topic, model="falcon", url='http://localhost:11434/api/generate', stream=False):
    prompt = create_story_prompt4(topic)
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json().get('response')
    else:
        return f"Error: Unable to generate a response. Status code: {response.status_code}"

