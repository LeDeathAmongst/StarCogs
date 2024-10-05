from discord import (
    AppCommandOptionType,
    ApplicationFlags,
    Attachment,
    CategoryChannel,
    ChannelFlags,
    Color,
    Colour,
    Emoji,
    ForumChannel,
    Guild,
    GuildSticker,
    Invite,
    Member,
    MemberCacheFlags,
    Message,
    MessageFlags,
    Object,
    PartialEmoji,
    PartialMessage,
    PublicUserFlags,
    Role,
    ScheduledEvent,
    StageChannel,
    Sticker,
    SystemChannelFlags,
    TextChannel,
    Thread,
    User,
    UserFlags,
    VoiceChannel,
)
from discord.ext.commands import (
    CategoryChannelConverter,
    ColorConverter,
    ColourConverter,
    EmojiConverter,
    FlagConverter,
    ForumChannelConverter,
    GuildConverter,
    GuildStickerConverter,
    InviteConverter,
    MemberConverter,
    MessageConverter,
    ObjectConverter,
    PartialEmojiConverter,
    PartialMessageConverter,
    RoleConverter,
    ScheduledEventConverter,
    StageChannelConverter,
    TextChannelConverter,
    ThreadConverter,
    UserConverter,
    VoiceChannelConverter,
)
from redbot.core.i18n import Translator
from redbot.core.utils.chat_formatting import box

_ = Translator("AutoDocs", __file__)


def get_converter_docstring(object):
    types = {
        "str": _('A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".'),
        "int": _("A number without decimal places."),
        "float": _("A number with or without decimal places."),
        "bool": _("Can be 1, 0, true, false, t, f"),
    }
    CONVERTERS = {
        Member: MemberConverter.__doc__,
        Emoji: EmojiConverter.__doc__,
        Guild: GuildConverter.__doc__,
        CategoryChannel: CategoryChannelConverter.__doc__,
        Invite: InviteConverter.__doc__,
        PartialEmoji: PartialEmojiConverter.__doc__,
        PartialMessage: PartialMessageConverter.__doc__,
        Message: MessageConverter.__doc__,
        User: UserConverter.__doc__,
        Role: RoleConverter.__doc__,
        TextChannel: TextChannelConverter.__doc__,
        VoiceChannel: VoiceChannelConverter.__doc__,
        StageChannel: StageChannelConverter.__doc__,
        Thread: ThreadConverter.__doc__,
        Color: ColorConverter.__doc__,
        Colour: ColourConverter.__doc__,
        Sticker: GuildStickerConverter.__doc__,
        GuildSticker: GuildStickerConverter.__doc__,
        Object: ObjectConverter.__doc__,
        ScheduledEvent: ScheduledEventConverter.__doc__,
        ForumChannel: ForumChannelConverter.__doc__,
        UserFlags: FlagConverter.__doc__,
        ChannelFlags: FlagConverter.__doc__,
        PublicUserFlags: FlagConverter.__doc__,
        SystemChannelFlags: FlagConverter.__doc__,
        ApplicationFlags: FlagConverter.__doc__,
        MessageFlags: FlagConverter.__doc__,
        MemberCacheFlags: FlagConverter.__doc__,
        int: box(types["int"]),
        float: box(types["float"]),
        bool: box(types["bool"]),
        str: box(types["str"]),
        AppCommandOptionType.string: box(types["str"]),
        AppCommandOptionType.integer: box(types["int"]),
        AppCommandOptionType.boolean: box(types["bool"]),
        AppCommandOptionType.user: MemberConverter.__doc__,
        AppCommandOptionType.channel: TextChannelConverter.__doc__,
        AppCommandOptionType.role: RoleConverter.__doc__,
        AppCommandOptionType.attachment: Attachment.__doc__,
    }
    return CONVERTERS.get(object)


CLASSCONVERTER = {
    AppCommandOptionType.string: str,
    AppCommandOptionType.integer: int,
    AppCommandOptionType.boolean: bool,
    AppCommandOptionType.user: Member,
    AppCommandOptionType.channel: TextChannel,
    AppCommandOptionType.role: Role,
    AppCommandOptionType.attachment: Attachment,
}

PRIVILEGES = {"user": 1, "mod": 2, "admin": 3, "guildowner": 4, "botowner": 5}
