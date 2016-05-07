class Status_bar:
    def __init__(self, template, hero):
        self.template = template
        self.hero = hero

    def render(self):
        render_list = []
        for line in self.template:
            render_list.append(line.format(hero=self.hero))
        return render_list


status_bar = [
    '**Level {hero.level}*****************************',
    '*HP={hero.heal_points} EX={hero.experience} AT={hero.attack} DF={hero.defend} MN={hero.money} OV={hero.overhand}',
    '**************************************'
]



