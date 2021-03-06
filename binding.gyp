{
	'targets': [
		{
			'target_name': 'NodeCoreAudio',
			'sources': [
				'NodeCoreAudio/AudioEngine.cpp',
				'NodeCoreAudio/NodeCoreAudio.cpp',
			],
			'include_dirs': [
				'<(module_root_dir)/NodeCoreAudio/',
				'<(module_root_dir)/portaudio/'
			],
			"conditions" : [
				[
					'OS!="win"', {
						"libraries" : [
							'-lportaudio'
						],
						'cflags!': [ '-fno-exceptions' ],
						'cflags_cc!': [ '-fno-exceptions' ]
					}
				],
				[
					'OS=="win"', {
						"include_dirs" : [ "gyp/include" ],
						"libraries" : [
							'<(module_root_dir)/gyp/lib/portaudio_x86.lib'
						]
					}
				]
			],
			
		}
	]
}