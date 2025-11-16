import pathlib
import re
from collections import defaultdict, OrderedDict

REPO = pathlib.Path(__file__).resolve().parents[1]
MONO_DIR = REPO / 'monologues'
GUIDE_DIR = REPO / 'vocal-energy'

# Metadata for emotional color categories
CATEGORIES = OrderedDict([
    ('crimson-command', {
        'name': 'Crimson Command',
        'summary': 'Fiery civic authority and battle-ready proclamations.',
        'description': 'Use this color whenever the speaker must sound like a commander, magistrate, or war leader rallying the crowd.',
        'keywords': ['authority', 'command', 'battle', 'trumpet', 'clarion', 'drill', 'bark', 'order', 'steel', 'martial', 'masters',
                     'public-address', 'edict', 'decree', 'proclamation', 'challenge', 'shock command', 'triumphant', 'crown',
                     'colossus', 'thunder', 'spear', 'arms', 'host', 'kings', 'captain', 'trumpeting', 'victory', 'bell-like',
                     'summon', 'alarm', 'standard', 'flag', 'war', 'marshal', 'charge', 'drum', 'pronouncement', 'authority weight',
                     'rhetorical pounding', 'snapped drill', 'steel-cold', 'ultimatum', 'snarling command', 'provocative questioning',
                     'taunting challenge', 'staccato condemnation', 'spitting consonants, high pitch', 'command bark',
                     'commanding breath', 'commanding empathy', 'commanding', 'appeal to crowd', 'public plea', 'preacher',
                     'sermon', 'sergeant', 'counting cadence', 'stone-hard cadence', 'bell-peal'],
        'resonance': OrderedDict([
            ('Larynx height', 'Keep the larynx neutral-to-low for a dark/round column that implies rank.'),
            ('Epilaryngeal (AES) “twang”', 'Add a firm AES narrowing to cut through space without shouting.'),
            ('Velum (nasality)', 'Keep the velum fully raised for a clear, non-nasal civic tone.'),
            ('Pharynx width', 'Maintain a moderately narrowed pharynx to focus the beam while retaining warmth.'),
            ('Tongue root', 'Stay neutral-to-slightly forward so consonants stay crisp under pressure.'),
            ('Jaw aperture', 'Open the jaw easily to let power bloom without clamp.'),
            ('Lip shape', 'Hold lips in a strong neutral line, rounding only on grand vowels.'),
            ('False vocal folds', 'Retract false folds aggressively to avoid harsh constriction.'),
            ('Vocal-fold adduction', 'Use solid, balanced adduction—never breathy, never pinched.'),
            ('Fold thickness (CT↔TA)', 'Favor thicker TA engagement for chesty weight, easing toward CT on high shouts.'),
            ('Breath pressure/flow', 'Drive a steady, compressed breath stream to keep the decree energized.')
        ])
    }),
    ('ember-rally', {
        'name': 'Ember Rally',
        'summary': 'Propulsive surges, urgent lifts, and crowd-stirring momentum.',
        'description': 'This color fuels crescendos, rising appeals, and any “on-your-feet” momentum swing.',
        'keywords': ['surge', 'rally', 'urgent', 'urgency', 'drive', 'driving', 'propel', 'crescendo', 'rising', 'rise', 'ignite',
                     'spark', 'bright', 'lift', 'uplift', 'soar', 'inflame', 'energ', 'coaxing', 'encourage', 'fervor', 'zeal',
                     'swell', 'flood', 'call to arms', 'stir', 'mutiny', 'drumbeat', 'press', 'breathless', 'charged', 'hammer',
                     'pounding', 'pulse', 'storm', 'rush', 'flare', 'sprint', 'propulsive', 'counting cadence, tessitura↗',
                     'word “mutiny” brightened', 'swell to bitterness', 'cataclysmic', 'explosive', 'sudden spark',
                     'tessitura↗', 'tessitura↗↗', 'high tessitura', 'tessitura↑', 'tessitura↗ slightly', 'alarm', 'surging',
                     'driving to verdict', 'driving decree', 'hammered repetition', 'breathless invocation', 'breathless gamble'],
        'resonance': OrderedDict([
            ('Larynx height', 'Allow the larynx to float mid-to-high for bright, energetic ping.'),
            ('Epilaryngeal (AES) “twang”', 'Narrow the AES enough to keep sparkle and projection.'),
            ('Velum (nasality)', 'Lift the velum fully so the sound stays clear as energy spikes.'),
            ('Pharynx width', 'Keep the pharynx mid-width so vowels stay agile even while excited.'),
            ('Tongue root', 'Stay neutral and buoyant; avoid retraction that would slow the line.'),
            ('Jaw aperture', 'Let the jaw swing freely with quick openings for rhythmic punches.'),
            ('Lip shape', 'Use flexible lips—slight spreads on bright syllables, quick rounding for momentum pivots.'),
            ('False vocal folds', 'Retract to maintain freedom even in fast, urgent phrases.'),
            ('Vocal-fold adduction', 'Aim for balanced adduction; enough closure for brilliance without choking airflow.'),
            ('Fold thickness (CT↔TA)', 'Blend CT tilt with TA depth so high pitches remain supported but gutsy.'),
            ('Breath pressure/flow', 'Pulse a steady but lively airflow; think constant “lean” rather than brute push.')
        ])
    }),
    ('obsidian-fury', {
        'name': 'Obsidian Fury',
        'summary': 'Menace, vengeance, and smoldering rage.',
        'description': 'Choose this when the voice must threaten, accuse, or unleash wrath with dark heat.',
        'keywords': ['fury', 'venom', 'snarl', 'growl', 'harsh', 'rage', 'anger', 'threat', 'thunder', 'wrath', 'spit', 'spitting',
                     'bitter', 'scorn', 'accus', 'blade', 'stab', 'kill', 'burn', 'blood', 'murder', 'curse', 'dark', 'grim', 'menace',
                     'pestilence', 'low growl', 'warning growl', 'warning', 'venomous', 'obsession', 'feral', 'savage', 'trap',
                     'snapping', 'sardonic hush', 'spitting denial', 'threat recalled', 'sobbing shout', 'voice cracking',
                     'ultimatum hiss', 'weight of betrayal', 'storm', 'cold ultimatum', 'shadow', 'glare', 'hammered rhythm',
                     'low burn', 'dagger', 'blade', 'blood', 'pounding vengeance', 'grim', 'ashen retrospection', 'dark relish',
                     'bitter litany', 'bitter confession', 'bitter epiphany', 'bitter scoff', 'bitter inventory'],
        'resonance': OrderedDict([
            ('Larynx height', 'Drop the larynx slightly for a darker, dangerous timbre.'),
            ('Epilaryngeal (AES) “twang”', 'Keep a narrowed AES so the bite still cuts through.'),
            ('Velum (nasality)', 'Seal the velum to avoid any nasal buzz that would blunt the threat.'),
            ('Pharynx width', 'Open the pharynx for cavernous heat and overtones.'),
            ('Tongue root', 'Slightly retract the tongue root to add grit, but don’t swallow vowels.'),
            ('Jaw aperture', 'Let the jaw hang open enough for resonance while keeping a clenched undertone.'),
            ('Lip shape', 'Use more spread or sneering lips to expose consonant attacks.'),
            ('False vocal folds', 'Allow a touch of false-fold engagement for texture, without full constriction.'),
            ('Vocal-fold adduction', 'Lean into firm adduction for a tight, searing core.'),
            ('Fold thickness (CT↔TA)', 'Favor thicker TA mass for chest-driven weight.'),
            ('Breath pressure/flow', 'Support with compressed breath so the fury simmers instead of shouts.')
        ])
    }),
    ('amber-irony', {
        'name': 'Amber Irony',
        'summary': 'Wry, sardonic, or subversively playful edges.',
        'description': 'Use for sarcasm, conspiratorial digs, and razor-smile commentary.',
        'keywords': ['irony', 'sardonic', 'mock', 'taunt', 'sneer', 'sarcasm', 'dry', 'wry', 'teasing', 'conspiratorial', 'playful',
                     'banter', 'lightness', 'mocking', 'sunlit sarcasm', 'amber', 'brittle politeness', 'knife-thin', 'blade',
                     'wit', 'hollow civility', 'bitter irony', 'brittle compliment', 'mock invocation', 'mocking awe',
                     'conspiratorial hush', 'conspiratorial whisper', 'conspiratorial tone', 'teasing affection', 'teasing reveal',
                     'taunting laughter', 'sardonic hush', 'sly', 'sneering', 'sardonic', 'scoff', 'contemptuous scoff', 'crisp edge',
                     'droll', 'bright irony'],
        'resonance': OrderedDict([
            ('Larynx height', 'Keep the larynx mid-to-high for a bright, cutting glaze.'),
            ('Epilaryngeal (AES) “twang”', 'Use a quick, precise AES pinch to highlight the sarcasm shimmer.'),
            ('Velum (nasality)', 'Velum mostly raised, but allow a trace of nasal buzz when you want smugness.'),
            ('Pharynx width', 'Slightly narrow the pharynx to focus the tone like a spotlight.'),
            ('Tongue root', 'Keep the tongue root neutral-to-forward for nimble diction.'),
            ('Jaw aperture', 'Maintain a moderate jaw opening that can snap shut for irony beats.'),
            ('Lip shape', 'Favor spread lips to telegraph the sly grin.'),
            ('False vocal folds', 'Fully retract to keep the tone clean and agile.'),
            ('Vocal-fold adduction', 'Use medium adduction—tight enough for sparkle, loose enough for quick pivots.'),
            ('Fold thickness (CT↔TA)', 'Lean toward thinner CT-driven folds for agile, heady resonance.'),
            ('Breath pressure/flow', 'Employ a lean, steady flow; think “needlepoint” rather than blast.')
        ])
    }),
    ('silver-resolve', {
        'name': 'Silver Resolve',
        'summary': 'Measured logic, ceremonial control, and forensic argument.',
        'description': 'Choose this for legal reasoning, formal address, or any line that must feel carefully weighed.',
        'keywords': ['measured', 'logic', 'forensic', 'calm', 'clinical', 'ceremonial', 'steady', 'deliberate', 'weigh', 'analysis',
                     'counting', 'reason', 'civic', 'public', 'inventory', 'list', 'formal', 'purpose', 'flat', 'neutral', 'statement',
                     'ceremonial ring', 'ceremonial correctness', 'ceremonial courtesy', 'ceremonial deference', 'ceremonial emptiness',
                     'ceremonial flatness', 'civic', 'analysis', 'measured cadence', 'measured logic', 'measured disdain',
                     'controlled syllogism', 'counting cadence', 'steady oath', 'steady promise', 'clarion opening', 'tessitura→',
                     'mid tessitura', 'tessitura→', 'tessitura→,', 'flat affect', 'even tone', 'clinical appraisal', 'civic spectacle'],
        'resonance': OrderedDict([
            ('Larynx height', 'Keep the larynx comfortably mid-level to avoid emotional extremes.'),
            ('Epilaryngeal (AES) “twang”', 'Maintain only a mild AES narrowing for intelligibility without excess bite.'),
            ('Velum (nasality)', 'Raise the velum for a clean, court-ready line.'),
            ('Pharynx width', 'Hold a medium pharyngeal width so tone feels grounded yet neutral.'),
            ('Tongue root', 'Let the tongue root stay neutral for precise consonants.'),
            ('Jaw aperture', 'Use a moderate jaw drop that supports articulate, even pacing.'),
            ('Lip shape', 'Keep lips neutral so vowels remain pure and uncolored.'),
            ('False vocal folds', 'Retract fully to keep the stream unobstructed.'),
            ('Vocal-fold adduction', 'Balance adduction—neither breathy nor clenched.'),
            ('Fold thickness (CT↔TA)', 'Stay in the middle mix; neither overly chesty nor too heady.'),
            ('Breath pressure/flow', 'Maintain consistent breath flow, as if reading official testimony.')
        ])
    }),
    ('cobalt-intimacy', {
        'name': 'Cobalt Intimacy',
        'summary': 'Soft confessions, whispered bargains, and personal pleas.',
        'description': 'Use for hushed admissions, secret-sharing, or any line meant for one trusted ear.',
        'keywords': ['soft', 'whisper', 'intimate', 'tender', 'plea', 'hush', 'quiet', 'gentle', 'supplicant', 'confession', 'murmur',
                     'breathy', 'caressing', 'private', 'secret', 'warning hush', 'submerged hush', 'soft drop', 'soft fade',
                     'soft gravity', 'soft sincerity', 'soft triumph', 'soft dread', 'softening', 'soft lament', 'soft marvel',
                     'soft promise', 'soft vow', 'soft praise', 'soft hush', 'soft awe', 'soft release', 'softening exhale', 'soft lilt',
                     'soft instruction', 'soft imagery', 'soft gloom', 'soft glow', 'soft plea', 'soft but unyielding', 'soft pivot',
                     'quiet invocation', 'quiet confession', 'supplicant fall', 'supplicant pride', 'whispered', 'voluptuous whisper',
                     'warning hush', 'subtle hush', 'sotto voce', 'low murmur', 'voice folding inward',
                     'voice hollowing', 'gentle', 'soft drop',
                     'soft dread', 'soft sincerity', 'soft vow', 'soft triumph'],
        'resonance': OrderedDict([
            ('Larynx height', 'Let the larynx settle low-to-neutral for smoky closeness.'),
            ('Epilaryngeal (AES) “twang”', 'Open the AES slightly so the tone stays velvety, not piercing.'),
            ('Velum (nasality)', 'Raise the velum but allow a hint of nasality if you want intimacy.'),
            ('Pharynx width', 'Keep the pharynx comfortably wide for warm, hushed vowels.'),
            ('Tongue root', 'Release the tongue root forward so vowels stay clear even at low volume.'),
            ('Jaw aperture', 'Maintain a relaxed, smaller jaw drop to suggest confidentiality.'),
            ('Lip shape', 'Round or neutral lips help the sound feel cushioned and secretive.'),
            ('False vocal folds', 'Retract to keep airflow free at the softer dynamic.'),
            ('Vocal-fold adduction', 'Use lighter adduction so the sound can hover without force.'),
            ('Fold thickness (CT↔TA)', 'Lean toward thinner folds (CT tilt) so pianissimo lines stay supported.'),
            ('Breath pressure/flow', 'Feed a gentle, continuous stream; imagine fogging a window.')
        ])
    }),
    ('violet-lament', {
        'name': 'Violet Lament',
        'summary': 'Grief, mourning, and exhausted sorrow.',
        'description': 'Choose this when the text sinks into loss, funereal recollection, or ache-filled retrospection.',
        'keywords': ['somber', 'lament', 'grief', 'mourning', 'sorrow', 'weary', 'despair', 'ash', 'funereal', 'tragic', 'tear',
                     'tears', 'wound', 'heart', 'cry', 'sob', 'lamenting', 'grieving', 'dirge', 'requiem', 'coffin', 'death', 'grave',
                     'mourning', 'wounded', 'bleed', 'sobbing', 'grave', 'tolling', 'ash', 'hollow', 'dust', 'funeral', 'loss',
                     'fallen', 'ruin', 'soft grief', 'somber awe', 'somber closure', 'ash', 'ashen', 'mourn', 'pity', 'weep', 'weeping',
                     'wound', 'blood', 'funereal weight', 'dirt', 'ground', 'slow confession', 'desolate', 'dust-choked', 'spent',
                     'storybook hush', 'dim resonance', 'hollow landing', 'tessitura↓', 'tessitura↓↓', 'falling tessitura', 'low growl of sorrow'],
        'resonance': OrderedDict([
            ('Larynx height', 'Keep the larynx low to let sorrow sound dark and round.'),
            ('Epilaryngeal (AES) “twang”', 'Leave the AES more open; too much ring feels insincere.'),
            ('Velum (nasality)', 'Velum mostly raised, but allow tiny leaks to mimic a sob if needed.'),
            ('Pharynx width', 'Hold the pharynx wide for a covered, mournful warmth.'),
            ('Tongue root', 'Let the tongue root relax or slightly retract to add ache.'),
            ('Jaw aperture', 'Use a heavy jaw drop so phrases can “fall” under their own weight.'),
            ('Lip shape', 'Round the lips gently; avoid aggressive spreads.'),
            ('False vocal folds', 'Keep them retracted but soft, allowing a hint of breathiness.'),
            ('Vocal-fold adduction', 'Moderate adduction—too much squeeze kills the lament.'),
            ('Fold thickness (CT↔TA)', 'Blend TA warmth with CT lift so the grief can both resonate and sigh.'),
            ('Breath pressure/flow', 'Slow, even airflow supports the sense of tolling inevitability.')
        ])
    }),
    ('verdant-compassion', {
        'name': 'Verdant Compassion',
        'summary': 'Nurturing kindness, warmth, and humane persuasion.',
        'description': 'Use for pastoral comfort, coaxing hope, or any invitation grounded in empathy.',
        'keywords': ['warm', 'comfort', 'compassion', 'nurture', 'love', 'affection', 'healing', 'kind', 'grace', 'blessing',
                     'care', 'gentle warmth', 'coaxing warmth', 'caressing', 'steady honesty',
                     'gracious', 'praise', 'blessing cadence', 'appeal landing', 'appeal', 'kind souls', 'sweet friends', 'good friends',
                     'soft gratitude', 'soft glow', 'soft marvel', 'soft devotion', 'kind', 'mercy', 'charity', 'blue sincerity',
                     'gentle persuasion', 'storytelling warmth', 'storyteller’s swell', 'storytelling glow', 'storybook cadence',
                     'storybook hush', 'good friends', 'sweet friends', 'compassionate', 'gracious drops'],
        'resonance': OrderedDict([
            ('Larynx height', 'Keep the larynx mid-to-low to sound rooted and kind.'),
            ('Epilaryngeal (AES) “twang”', 'Use only a gentle AES pinch so the tone stays round yet audible.'),
            ('Velum (nasality)', 'Raise the velum for clear warmth, letting just a hint drop if you want tenderness.'),
            ('Pharynx width', 'Maintain a wide, open pharynx for enveloping resonance.'),
            ('Tongue root', 'Keep the tongue root relaxed and slightly forward for pure vowels.'),
            ('Jaw aperture', 'Let the jaw release so the sound feels generous.'),
            ('Lip shape', 'Favor rounded or heart-shaped lips that feel embracing.'),
            ('False vocal folds', 'Retract to keep everything free and compassionate.'),
            ('Vocal-fold adduction', 'Balanced-to-light closure keeps the tone buoyant.'),
            ('Fold thickness (CT↔TA)', 'Blend thinner folds with a hint of TA to keep warmth without heaviness.'),
            ('Breath pressure/flow', 'Support with a buoyant, steady airflow that feels like a hand on the shoulder.')
        ])
    }),
    ('celestial-awe', {
        'name': 'Celestial Awe',
        'summary': 'Devotional, visionary, and transcendent imagery.',
        'description': 'Choose this for oaths, prayers, prophecies, and moments that look beyond the mortal world.',
        'keywords': ['awe', 'vision', 'prophecy', 'devotional', 'oath', 'mystic', 'divine', 'holy', 'prayer', 'reverent', 'wonder',
                     'angel', 'gods', 'heaven', 'sacred', 'reverent resonance', 'quiet invocation', 'blessing', 'oath', 'vow',
                     'lifted vowels', 'heroic tilt', 'devotional cadence', 'reverent', 'god', 'celestial', 'heaven', 'sublime',
                     'final oath', 'supplicant pride', 'reverent hush', 'grace', 'holy', 'sacrifice', 'sacred blood'],
        'resonance': OrderedDict([
            ('Larynx height', 'Let the larynx float neutral-to-slightly high to suggest uplift.'),
            ('Epilaryngeal (AES) “twang”', 'Use a clear AES narrowing for bell-like brilliance without strain.'),
            ('Velum (nasality)', 'Velum tall and sealed to keep the tone pure and ringing.'),
            ('Pharynx width', 'Stretch the pharynx vertically for cathedral-like space.'),
            ('Tongue root', 'Keep the tongue root neutral or gently forward to maintain clarity.'),
            ('Jaw aperture', 'Allow a released, almost awe-struck jaw drop.'),
            ('Lip shape', 'Round or sculpt the lips to create a haloed resonance.'),
            ('False vocal folds', 'Retract completely so the sound stays luminous.'),
            ('Vocal-fold adduction', 'Aim for balanced, centered adduction—firm but never pressed.'),
            ('Fold thickness (CT↔TA)', 'Favor thinner folds (CT tilt) for shimmer, blending TA for weighty vows.'),
            ('Breath pressure/flow', 'Sustain a low, anchored breath flow to keep the line floating.')
        ])
    })
])

DEFAULT_CATEGORY = 'silver-resolve'

# Table string
TABLE_MD = """| Resonator / control            | Spectrum (← →)              | Tonal effect (← →)                         |
| ------------------------------ | --------------------------- | ------------------------------------------ |
| **Larynx height**              | low → high                  | dark/round → bright/edgy                   |
| **Epilaryngeal (AES) “twang”** | open → narrowed             | soft/hollow → ring/projection              |
| **Velum (nasality)**           | lowered → raised            | nasal/buzzy → clear/non-nasal              |
| **Pharynx width**              | wide → narrower             | warm/covered → focused/bright              |
| **Tongue root** †              | retracted → forward/neutral | woofy/muffled → bright/clear               |
| **Jaw aperture** †             | small → larger (easy)       | thin/closed → fuller/warm                  |
| **Lip shape** †                | spread → rounded/protruded  | bright → dark/rich                         |
| **False vocal folds**          | constricted → retracted     | harsh/noisy → clean/free                   |
| **Vocal-fold adduction**       | less → more                 | airy/soft → tight/grainy (best = balanced) |
| **Fold thickness (CT↔TA)**     | thin → thick                | heady/sparkly → chesty/warm                |
| **Breath pressure/flow**       | low → higher/steady         | weak/flat → energetic/brassy               |

† May alter vowel quality if overdone—use subtly.
"""

INTRO_MD = """# Vocal Energy Guide

Actors requested a repeatable way to interpret every bracketed intention/energy/tone cue across these monologues. The guide below introduces the shared resonator spectrum, then links to each emotional-color grouping so you can dial the exact setup before reviewing a monologue’s `Vocal Energy Guidance` section.
"""

USAGE_MD = """## How to use this guide

1. Review the spectrum table to remind yourself what happens when you shift each control point.
2. Open any color page from the directory to see how that emotional hue manipulates the spectrum.
3. Jump into a monologue page and scroll to `## Vocal Energy Guidance`. Each category listed there links back to its color page so you can reset your setup between cue clusters.
"""

# Build color directory content
def write_vocal_energy_docs():
    GUIDE_DIR.mkdir(exist_ok=True)
    color_links = []
    for slug, meta in CATEGORIES.items():
        color_links.append(f"- [{meta['name']}](./{slug}.md) — {meta['summary']}")
    color_dir_md = "## Emotional color directory\n\n" + "\n".join(color_links) + "\n"
    (GUIDE_DIR / 'README.md').write_text("\n\n".join([INTRO_MD.strip(), TABLE_MD.strip(), color_dir_md.strip(), USAGE_MD.strip()]) + "\n")
    for slug, meta in CATEGORIES.items():
        path = GUIDE_DIR / f"{slug}.md"
        lines = [f"# {meta['name']}", '', f"_{meta['summary']}_", '', meta['description'], '', '## Resonator and control targets', '']
        for control, guidance in meta['resonance'].items():
            lines.append(f"- **{control}:** {guidance}")
        lines.append('')
        lines.append('## When to reach for this color')
        lines.append('')
        lines.append('These cues typically appear anywhere you see this color referenced inside the monologue files. Let the vocal setup above prepare the tessitura, then match the on-page bracketed instructions for nuance.')
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('Return to the [Vocal Energy Guide](./README.md) or jump into any monologue’s `Vocal Energy Guidance` list to see where this color occurs.')
        lines.append('')
        path.write_text("\n".join(lines))


# Helper to categorize cues
keyword_map = {slug: [kw.lower() for kw in data['keywords']] for slug, data in CATEGORIES.items()}

category_order = list(CATEGORIES.keys())

def categorize(cue: str) -> str:
    text = cue.lower()
    for slug in category_order:
        for kw in keyword_map[slug]:
            if not kw:
                continue
            if re.fullmatch(r'[a-z\s]+', kw):
                pattern = r'\b' + re.escape(kw) + r'\b'
                if re.search(pattern, text):
                    return slug
            else:
                if kw in text:
                    return slug
    return DEFAULT_CATEGORY

def extract_cues():
    mon_cues = {}
    for path in sorted(MONO_DIR.glob('*.md')):
        cues = []
        in_perf = False
        for line in path.read_text().splitlines():
            if line.startswith('**IPA'):
                in_perf = False
            if line.strip() == 'Performance Line':
                in_perf = True
                continue
            if in_perf:
                match = re.match(r'\[([^\]]+)\]', line.strip())
                if match:
                    cues.append(match.group(1).strip())
        mon_cues[path] = cues
    return mon_cues


def apply_guidance_sections(mon_cues):
    for path, cues in mon_cues.items():
        if not cues:
            continue
        grouped = OrderedDict()
        for cue in cues:
            slug = categorize(cue)
            grouped.setdefault(slug, []).append(cue)
        if not grouped:
            continue
        section_lines = ['## Vocal Energy Guidance', '', 'Consult the [Vocal Energy guide](../vocal-energy/README.md) for the full spectrum and adjustment recipes.', '']
        for slug in category_order:
            if slug not in grouped:
                continue
            meta = CATEGORIES[slug]
            section_lines.append(f"### {meta['name']} — {meta['summary']}")
            section_lines.append(f"Use the [{meta['name']}](../vocal-energy/{slug}.md) setup for these cues:")
            section_lines.append('')
            for cue in grouped[slug]:
                section_lines.append(f"- `{cue}`")
            section_lines.append('')
        section_text = "\n".join(section_lines).rstrip() + "\n"
        content = path.read_text().rstrip()
        split_token = '\n## Vocal Energy Guidance'
        if split_token in content:
            content = content.split(split_token)[0].rstrip()
        content = content + '\n\n' + section_text
        path.write_text(content + '\n')


def update_readme():
    readme_path = REPO / 'README.md'
    readme = readme_path.read_text()
    link_block = "## Vocal Energy Resources\n\n- [Vocal Energy Guide](vocal-energy/README.md)"
    if 'Vocal Energy Guide' not in readme:
        readme = link_block + "\n\n" + readme
        readme_path.write_text(readme)


def main():
    write_vocal_energy_docs()
    mon_cues = extract_cues()
    apply_guidance_sections(mon_cues)
    update_readme()


if __name__ == '__main__':
    main()
