<template>
	<div style="padding: 10px;">
		<top></top>
		<br /><br />
		<div>
			<div style="display: flex;justify-items: center;align-items: flex-end;">
				<div style="margin-left: 20px;">
					<el-select v-model="value" clearable placeholder="请选择行业名称">
						<el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
						</el-option>
					</el-select>
				</div>
				<div style="margin-left: 20px;">
					<el-button style="width: 100px;" type="primary" @click="getinfo()">查看</el-button>
				</div>
				<div style="margin-left: 20px;line-height: 25px;">
					<router-link to="/createtable">返回</router-link>
				</div>
			</div>
			<div style="margin-top: 30px;">
				<div v-show="data==''" style="color: #b1b1b1;text-align: center;margin-top: 10%;height: 300px;">
					请选择行业名称点击查看！
				</div>
			</div>
			<div style="margin-top: 30px;" v-show="isedit">
				<el-input  type="textarea" :rows="16" placeholder="请输入内容" v-model="data">
				</el-input>
				<div style="text-align: center;display: flex;justify-content: center;margin-top: 20px;">
					<el-button style="width: 150px;" type="primary" @click="savedatabase()">物理化</el-button>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					<el-button style="width: 150px;" type="primary" @click="download()">下载</el-button>
				</div>
			</div>
		</div>
		<div style="height: 100px;">

		</div>
		<foot></foot>
	</div>
</template>

<script>
	import top from '../components/top.vue'
	import foot from '../components/footer.vue'
	// 下载文件
	function download(res) {
		let blob = new Blob([res.data], {
			type: "application/vnd.ms-excel"
		}); //type是文件类，详情可以参阅blob文件类型
		// 创建新的URL并指向File对象或者Blob对象的地址
		const blobURL = window.URL.createObjectURL(blob)
		// 创建a标签，用于跳转至下载链接
		const tempLink = document.createElement('a')
		tempLink.style.display = 'none'
		tempLink.href = blobURL
		tempLink.setAttribute('download', decodeURI(res.headers['content-disposition'].split(';')[1].split('=')[1]))
		// 兼容：某些浏览器不支持HTML5的download属性
		if (typeof tempLink.download === 'undefined') {
			tempLink.setAttribute('target', '_blank')
		}
		// 挂载a标签
		document.body.appendChild(tempLink)
		tempLink.click()
		document.body.removeChild(tempLink)
		// 释放blob URL地址
		window.URL.revokeObjectURL(blobURL)
	}
	export default {
		data() {
			return {
				options: [{
						value: '国民经济核算',
						label: '国民经济核算'
					}, {
						value: '固定资产投资',
						label: '固定资产投资'
					}, {
						value: '对外经济贸易',
						label: '对外经济贸易'
					}, {
						value: '价格',
						label: '价格'
					}, {
						value: '财政',
						label: '财政'
					},
					{
						value: '金融业',
						label: '金融业'
					},
					{
						value: '保险业',
						label: '保险业'
					},
					{
						value: '农业',
						label: '农业'
					},
					{
						value: '工业',
						label: '工业'
					},
					{
						value: '建筑业',
						label: '建筑业'
					}, {
						value: '科技',
						label: '科技'
					}, {
						value: '能源',
						label: '能源'
					}, {
						value: '交通运输',
						label: '交通运输'
					}, {
						value: '房地产',
						label: '房地产'
					}, {
						value: '批发与零售',
						label: '批发与零售'
					}, {
						value: '经济安全保障',
						label: '经济安全保障'
					}, {
						value: '人口',
						label: '人口'
					},
					{
						value: '就业人员和工资',
						label: '就业人员和工资'
					}, {
						value: '人民生活',
						label: '人民生活'
					}, {
						value: '生态环境保护',
						label: '生态环境保护'
					}, {
						value: '绿色生态',
						label: '绿色生态'
					}, {
						value: '邮电和软件业',
						label: '邮电和软件业'
					}, {
						value: '住宿和餐饮业',
						label: '住宿和餐饮业'
					}, {
						value: '旅游业',
						label: '旅游业'
					}, {
						value: '教育',
						label: '教育'
					}, {
						value: '社会服务',
						label: '社会服务'
					}
				],
				value: '',
				data: '',
				isedit: false
			}
		},
		components: {
			top,
			foot
		},
		methods: {
			getinfo() {
				let data = {
					hangye: this.value
				}
				this.$axios.get(this.$https + "/look?hangye="+this.value, this.$qs.stringify(data)).then(res => {
					if (res.status == 200) {
						this.isedit = true
						this.data = res.data
					} else {
						this.$message.error('未找到结果！');
					}
				}).catch(res => {
					this.$message.error('未找到结果！');
				})
			},
			savedatabase(){
				let data = {
					sql:this.data
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					if(res.status==500){
						this.$message({ message:'执行成功,为保证准确性，请到数据库查看！',type: 'success'});
					}else{
						this.$message.error( '保存失败！');
					}
				}).catch(res=>{
					console(res)
				})
				this.$message({ message:'执行成功,为保证准确性，请到数据库查看！',type: 'success'});
			},
			download() {
				let data = {
					hangye: this.value
				}
				this.$axios({
					method: 'get',
					url: this.$https + '/download?hangye=' + this.value,
					responseType: 'blob'
				}).then(res => {
					const {
						data
					} = res
					const blob = new Blob([data])
					let disposition = decodeURI(res.headers['content-disposition'])
					// 从响应头中获取文件名称
					let fileName = this.value + '.txt'
					if ('download' in document.createElement('a')) {
						// 非IE下载
						const elink = document.createElement('a')
						elink.download = fileName
						elink.style.display = 'none'
						elink.href = URL.createObjectURL(blob)
						document.body.appendChild(elink)
						elink.click()
						URL.revokeObjectURL(elink.href) // 释放URL 对象
			  	document.body.removeChild(elink)
					} else {
						// IE10+下载
						navigator.msSaveBlob(blob, fileName)
					}
				}).catch((error) => {
					console.log(error)
				})
			}

		}
	}
</script>

<style>
</style>
